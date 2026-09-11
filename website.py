"""Defines names.brodie.id.au website infrastructure using AWS CDK."""

from pathlib import Path

import aws_cdk as cdk
import aws_cdk.aws_certificatemanager as acm
import aws_cdk.aws_cloudfront as cloudfront
import aws_cdk.aws_cloudfront_origins as cloudfront_origins
import aws_cdk.aws_route53 as route53
import aws_cdk.aws_route53_targets as route53_targets
import aws_cdk.aws_s3 as s3
import aws_cdk.aws_s3_deployment as s3_deployment

# Path to html-wasm export, relative to this module.
build_path = Path(__file__).parent / "dist"


class App(cdk.App):
    def __init__(self) -> None:
        super().__init__()
        Website(self, id="Website")


class Website(cdk.Stack):
    """names.brodie.id.au website stack."""

    domain_name = "names.brodie.id.au"

    def __init__(self, scope, id: str) -> None:
        super().__init__(
            scope,
            id,
            description="names.brodie.id.au website",
            # CloudFront cert must be in us-east-1, put the stack there
            env=cdk.Environment(region="us-east-1"),
        )

        # This bucket contains static website files.
        bucket = s3.Bucket(
            scope=self,
            id="Bucket",
        )

        # Reference existing hosted zone.
        hosted_zone = route53.HostedZone.from_hosted_zone_attributes(
            scope=self,
            id="HostedZone",
            hosted_zone_id="Z0932427366G4DNP1CWB",
            zone_name="brodie.id.au",
        )

        # CloudFront distribution certificate.
        certificate = acm.Certificate(
            scope=self,
            id="Certificate",
            domain_name=self.domain_name,
            validation=acm.CertificateValidation.from_dns(hosted_zone),
        )

        # Create a CloudFront distribution that serves content from our S3 origin.
        distribution = cloudfront.Distribution(
            scope=self,
            id="Distribution",
            default_behavior=cloudfront.BehaviorOptions(
                origin=cloudfront_origins.S3BucketOrigin.with_origin_access_control(
                    bucket
                ),
                viewer_protocol_policy=cloudfront.ViewerProtocolPolicy.REDIRECT_TO_HTTPS,
            ),
            certificate=certificate,
            default_root_object="index.html",
            domain_names=[self.domain_name],
        )

        # Populate bucket with files from website export directory.
        s3_deployment.BucketDeployment(
            scope=self,
            id="BucketDeployment",
            destination_bucket=bucket,
            sources=[s3_deployment.Source.asset(str(build_path))],
            # Invalidate CloudFront distribution cache on change.
            distribution=distribution,
        )

        # Create an alias record for the CloudFront distribution.
        route53.ARecord(
            scope=self,
            id="Alias",
            target=route53.RecordTarget.from_alias(
                route53_targets.CloudFrontTarget(distribution)
            ),
            zone=hosted_zone,
            record_name=self.domain_name,
        )


if __name__ == "__main__":
    App().synth()
