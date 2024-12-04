"""# Names

An API for naming things

This [blog post](https://mnx.io/blog/a-proper-server-naming-scheme/) introduces
Oren Tirosh's mnemonic encoding
[project](http://web.archive.org/web/20090918202746/http://tothink.com/mnemonic/wordlist.html)

You can copy the raw mnemonic `wordlist.txt` file to your clipboard:

```bash
$ curl https://web.archive.org/web/20091003023412if_/http://tothink.com:80/mnemonic/wordlist.txt | pbcopy
```

I've pasted its contents further below. Here's what we know:

- There are 1633 words.

      >>> len(words)
      1633

- Words are not sorted.

      >>> sorted(words) == words
      False

- The first word is _acrobat_.

      >>> words[0]
      'acrobat'

- And the final word is _yes_.

      >>> words[-1]
      'yes'


## `wordlist.txt`

       Wordlist ver 0.732 - EXPECT INCOMPATIBLE CHANGES;
      acrobat  africa   alaska   albert   albino   album
      alcohol  alex     alpha    amadeus  amanda   amazon
      america  analog   animal   antenna  antonio  apollo
      april    aroma    artist   aspirin  athlete  atlas
      banana   bandit   banjo    bikini   bingo    bonus
      camera   canada   carbon   casino   catalog  cinema
      citizen  cobra    comet    compact  complex  context
      credit   critic   crystal  culture  david    delta
      dialog   diploma  doctor   domino   dragon   drama
      extra    fabric   final    focus    forum    galaxy
      gallery  global   harmony  hotel    humor    index
      japan    kilo     lemon    liter    lotus    mango
      melon    menu     meter    metro    mineral  model
      music    object   piano    pirate   plastic  radio
      report   signal   sport    studio   subject  super
      tango    taxi     tempo    tennis   textile  tokyo
      total    tourist  video    visa     academy  alfred
      atlanta  atomic   barbara  bazaar   brother  budget
      cabaret  cadet    candle   capsule  caviar   channel
      chapter  circle   cobalt   comrade  condor   crimson
      cyclone  darwin   declare  denver   desert   divide
      dolby    domain   double   eagle    echo     eclipse
      editor   educate  edward   effect   electra  emerald
      emotion  empire   eternal  evening  exhibit  expand
      explore  extreme  ferrari  forget   freedom  friday
      fuji     galileo  genesis  gravity  habitat  hamlet
      harlem   helium   holiday  hunter   ibiza    iceberg
      imagine  infant   isotope  jackson  jamaica  jasmine
      java     jessica  kitchen  lazarus  letter   license
      lithium  loyal    lucky    magenta  manual   marble
      maxwell  mayor    monarch  monday   money    morning
      mother   mystery  native   nectar   nelson   network
      nikita   nobel    nobody   nominal  norway   nothing
      number   october  office   oliver   opinion  option
      order    outside  package  pandora  panther  papa
      pattern  pedro    pencil   people   phantom  philips
      pioneer  pluto    podium   portal   potato   process
      proxy    pupil    python   quality  quarter  quiet
      rabbit   radical  radius   rainbow  ramirez  ravioli
      raymond  respect  respond  result   resume   richard
      river    roger    roman    rondo    sabrina  salary
      salsa    sample   samuel   saturn   savage   scarlet
      scorpio  sector   serpent  shampoo  sharon   silence
      simple   society  sonar    sonata   soprano  sparta
      spider   sponsor  abraham  action   active   actor
      adam     address  admiral  adrian   agenda   agent
      airline  airport  alabama  aladdin  alarm    algebra
      alibi    alice    alien    almond   alpine   amber
      amigo    ammonia  analyze  anatomy  angel    annual
      answer   apple    archive  arctic   arena    arizona
      armada   arnold   arsenal  arthur   asia     aspect
      athena   audio    august   austria  avenue   average
      axiom    aztec    bagel    baker    balance  ballad
      ballet   bambino  bamboo   baron    basic    basket
      battery  belgium  benefit  berlin   bermuda  bernard
      bicycle  binary   biology  bishop   blitz    block
      blonde   bonjour  boris    boston   bottle   boxer
      brandy   bravo    brazil   bridge   british  bronze
      brown    bruce    bruno    brush    burger   burma
      cabinet  cactus   cafe     cairo    calypso  camel
      campus   canal    cannon   canoe    cantina  canvas
      canyon   capital  caramel  caravan  career   cargo
      carlo    carol    carpet   cartel   cartoon  castle
      castro   cecilia  cement   center   century  ceramic
      chamber  chance   change   chaos    charlie  charm
      charter  cheese   chef     chemist  cherry   chess
      chicago  chicken  chief    china    cigar    circus
      city     clara    classic  claudia  clean    client
      climax   clinic   clock    club     cockpit  coconut
      cola     collect  colombo  colony   color    combat
      comedy   command  company  concert  connect  consul
      contact  contour  control  convert  copy     corner
      corona   correct  cosmos   couple   courage  cowboy
      craft    crash    cricket  crown    cuba     dallas
      dance    daniel   decade   decimal  degree   delete
      deliver  delphi   deluxe   demand   demo     denmark
      derby    design   detect   develop  diagram  diamond
      diana    diego    diesel   diet     digital  dilemma
      direct   disco    disney   distant  dollar   dolphin
      donald   drink    driver   dublin   duet     dynamic
      earth    east     ecology  economy  edgar    egypt
      elastic  elegant  element  elite    elvis    email
      empty    energy   engine   english  episode  equator
      escape   escort   ethnic   europe   everest  evident
      exact    example  exit     exotic   export   express
      factor   falcon   family   fantasy  fashion  fiber
      fiction  fidel    fiesta   figure   film     filter
      finance  finish   finland  first    flag     flash
      florida  flower   fluid    flute    folio    ford
      forest   formal   formula  fortune  forward  fragile
      france   frank    fresh    friend   frozen   future
      gabriel  gamma    garage   garcia   garden   garlic
      gemini   general  genetic  genius   germany  gloria
      gold     golf     gondola  gong     good     gordon
      gorilla  grand    granite  graph    green    group
      guide    guitar   guru     hand     happy    harbor
      harvard  havana   hawaii   helena   hello    henry
      hilton   history  horizon  house    human    icon
      idea     igloo    igor     image    impact   import
      india    indigo   input    insect   instant  iris
      italian  jacket   jacob    jaguar   janet    jargon
      jazz     jeep     john     joker    jordan   judo
      jumbo    june     jungle   junior   jupiter  karate
      karma    kayak    kermit   king     koala    korea
      labor    lady     lagoon   laptop   laser    latin
      lava     lecture  left     legal    level    lexicon
      liberal  libra    lily     limbo    limit    linda
      linear   lion     liquid   little   llama    lobby
      lobster  local    logic    logo     lola     london
      lucas    lunar    machine  macro    madam    madonna
      madrid   maestro  magic    magnet   magnum   mailbox
      major    mama     mambo    manager  manila   marco
      marina   market   mars     martin   marvin   mary
      master   matrix   maximum  media    medical  mega
      melody   memo     mental   mentor   mercury  message
      metal    meteor   method   mexico   miami    micro
      milk     million  minimum  minus    minute   miracle
      mirage   miranda  mister   mixer    mobile   modem
      modern   modular  moment   monaco   monica   monitor
      mono     monster  montana  morgan   motel    motif
      motor    mozart   multi    museum   mustang  natural
      neon     nepal    neptune  nerve    neutral  nevada
      news     next     ninja    nirvana  normal   nova
      novel    nuclear  numeric  nylon    oasis    observe
      ocean    octopus  olivia   olympic  omega    opera
      optic    optimal  orange   orbit    organic  orient
      origin   orlando  oscar    oxford   oxygen   ozone
      pablo    pacific  pagoda   palace   pamela   panama
      pancake  panda    panel    panic    paradox  pardon
      paris    parker   parking  parody   partner  passage
      passive  pasta    pastel   patent   patient  patriot
      patrol   pegasus  pelican  penguin  pepper   percent
      perfect  perfume  period   permit   person   peru
      phone    photo    picasso  picnic   picture  pigment
      pilgrim  pilot    pixel    pizza    planet   plasma
      plaza    pocket   poem     poetic   poker    polaris
      police   politic  polo     polygon  pony     popcorn
      popular  postage  precise  prefix   premium  present
      price    prince   printer  prism    private  prize
      product  profile  program  project  protect  proton
      public   pulse    puma     pump     pyramid  queen
      radar    ralph    random   rapid    rebel    record
      recycle  reflex   reform   regard   regular  relax
      reptile  reverse  ricardo  right    ringo    risk
      ritual   robert   robot    rocket   rodeo    romeo
      royal    russian  safari   salad    salami   salmon
      salon    salute   samba    sandra   santana  sardine
      school   scoop    scratch  screen   script   scroll
      second   secret   section  segment  select   seminar
      senator  senior   sensor   serial   service  shadow
      sharp    sheriff  shock    short    shrink   sierra
      silicon  silk     silver   similar  simon    single
      siren    slang    slogan   smart    smoke    snake
      social   soda     solar    solid    solo     sonic
      source   soviet   special  speed    sphere   spiral
      spirit   spring   static   status   stereo   stone
      stop     street   strong   student  style    sultan
      susan    sushi    suzuki   switch   symbol   system
      tactic   tahiti   talent   tarzan   telex    texas
      theory   thermos  tiger    titanic  tomato   topic
      tornado  toronto  torpedo  totem    tractor  traffic
      transit  trapeze  travel   tribal   trick    trident
      trilogy  tripod   tropic   trumpet  tulip    tuna
      turbo    twist    ultra    uniform  union    uranium
      vacuum   valid    vampire  vanilla  vatican  velvet
      ventura  venus    vertigo  veteran  victor   vienna
      viking   village  vincent  violet   violin   virtual
      virus    vision   visitor  visual   vitamin  viva
      vocal    vodka    volcano  voltage  volume   voyage
      water    weekend  welcome  western  window   winter
      wizard   wolf     world    xray     yankee   yoga
      yogurt   yoyo     zebra    zero     zigzag   zipper
      zodiac   zoom     acid     adios    agatha   alamo
      alert    almanac  aloha    andrea   anita    arcade
      aurora   avalon   baby     baggage  balloon  bank
      basil    begin    biscuit  blue     bombay   botanic
      brain    brenda   brigade  cable    calibre  carmen
      cello    celtic   chariot  chrome   citrus   civil
      cloud    combine  common   cool     copper   coral
      crater   cubic    cupid    cycle    depend   door
      dream    dynasty  edison   edition  enigma   equal
      eric     event    evita    exodus   extend   famous
      farmer   food     fossil   frog     fruit    geneva
      gentle   george   giant    gilbert  gossip   gram
      greek    grille   hammer   harvest  hazard   heaven
      herbert  heroic   hexagon  husband  immune   inca
      inch     initial  isabel   ivory    jason    jerome
      joel     joshua   journal  judge    juliet   jump
      justice  kimono   kinetic  leonid   leopard  lima
      maze     medusa   member   memphis  michael  miguel
      milan    mile     miller   mimic    mimosa   mission
      monkey   moral    moses    mouse    nancy    natasha
      nebula   nickel   nina     noise    orchid   oregano
      origami  orinoco  orion    othello  paper    paprika
      prelude  prepare  pretend  promise  prosper  provide
      puzzle   remote   repair   reply    rival    riviera
      robin    rose     rover    rudolf   saga     sahara
      scholar  shelter  ship     shoe     sigma    sister
      sleep    smile    spain    spark    split    spray
      square   stadium  star     storm    story    strange
      stretch  stuart   subway   sugar    sulfur   summer
      survive  sweet    swim     table    taboo    target
      teacher  telecom  temple   tibet    ticket   tina
      today    toga     tommy    tower    trivial  tunnel
      turtle   twin     uncle    unicorn  unique   update
      valery   vega     version  voodoo   warning  william
      wonder   year     yellow   young    absent   absorb
      absurd   accent   alfonso  alias    ambient  anagram
      andy     anvil    appear   apropos  archer   ariel
      armor    arrow    austin   avatar   axis     baboon
      bahama   bali     balsa    barcode  bazooka  beach
      beast    beatles  beauty   before   benny    betty
      between  beyond   billy    bison    blast    bless
      bogart   bonanza  book     border   brave    bread
      break    broken   bucket   buenos   buffalo  bundle
      button   buzzer   byte     caesar   camilla  canary
      candid   carrot   cave     chant    child    choice
      chris    cipher   clarion  clark    clever   cliff
      clone    conan    conduct  congo    costume  cotton
      cover    crack    current  danube   data     decide
      deposit  desire   detail   dexter   dinner   donor
      druid    drum     easy     eddie    enjoy    enrico
      epoxy    erosion  except   exile    explain  fame
      fast     father   felix    field    fiona    fire
      fish     flame    flex     flipper  float    flood
      floor    forbid   forever  fractal  frame    freddie
      front    fuel     gallop   game     garbo    gate
      gelatin  gibson   ginger   giraffe  gizmo    glass
      goblin   gopher   grace    gray     gregory  grid
      griffin  ground   guest    gustav   gyro     hair
      halt     harris   heart    heavy    herman   hippie
      hobby    honey    hope     horse    hostel   hydro
      imitate  info     ingrid   inside   invent   invest
      invite   ivan     james    jester   jimmy    join
      joseph   juice    julius   july     kansas   karl
      kevin    kiwi     ladder   lake     laura    learn
      legacy   legend   lesson   life     light    list
      locate   lopez    lorenzo  love     lunch    malta
      mammal   margin   margo    marion   mask     match
      mayday   meaning  mercy    middle   mike     mirror
      modest   morph    morris   mystic   nadia    nato
      navy     needle   neuron   never    newton   nice
      night    nissan   nitro    nixon    north    oberon
      octavia  ohio     olga     open     opus     orca
      oval     owner    page     paint    palma    parent
      parlor   parole   paul     peace    pearl    perform
      phoenix  phrase   pierre   pinball  place    plate
      plato    plume    pogo     point    polka    poncho
      powder   prague   press    presto   pretty   prime
      promo    quest    quick    quiz     quota    race
      rachel   raja     ranger   region   remark   rent
      reward   rhino    ribbon   rider    road     rodent
      round    rubber   ruby     rufus    sabine   saddle
      sailor   saint    salt     scale    scuba    season
      secure   shake    shallow  shannon  shave    shelf
      sherman  shine    shirt    side     sinatra  sincere
      size     slalom   slow     small    snow     sofia
      song     sound    south    speech   spell    spend
      spoon    stage    stamp    stand    state    stella
      stick    sting    stock    store    sunday   sunset
      support  supreme  sweden   swing    tape     tavern
      think    thomas   tictac   time     toast    tobacco
      tonight  torch    torso    touch    toyota   trade
      tribune  trinity  triton   truck    trust    type
      under    unit     urban    urgent   user     value
      vendor   venice   verona   vibrate  virgo    visible
      vista    vital    voice    vortex   waiter   watch
      wave     weather  wedding  wheel    whiskey  wisdom
      android  annex    armani   cake     confide  deal
      define   dispute  genuine  idiom    impress  include
      ironic   null     nurse    obscure  prefer   prodigy
      ego      fax      jet      job      rio      ski
      yes
"""

import random

import typer

# Extract words from raw word list.
words = tuple(
    word
    for line in
    # Slice above docstring from first mnemonic onwards.
    __doc__[__doc__.index("\n      acrobat") :].splitlines()
    # Split each line into words.
    for word in line.split()
)


def sample_words(
    seed: int | float | str | bytes | bytearray, start: int, stop: int
) -> list[str]:
    """Returns a slice of randomly shuffled `words`.

    `seed` - shuffle `words` the same way in future
    `start` - slice start
    `stop` - slice stop
    """
    random.seed(seed)
    return random.sample(population=words, k=len(words))[start:stop]


if __name__ == "__main__":

    def wrapper(seed: str = "", count: int = 5, offset: int = 0) -> None:
        """Display `count` names randomised with `seed` starting from `offset`."""
        print(
            dict(
                enumerate(
                    sample_words(seed, start=offset, stop=offset + count), start=offset
                )
            )
        )

    typer.run(wrapper)  # TODO: add CLI test
