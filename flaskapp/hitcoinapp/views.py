from flask import render_template
from hitcoinapp import app
from flask import request
import datetime
from sqlalchemy import create_engine
from sqlalchemy_utils import database_exists, create_database

import pandas as pd
import psycopg2
from hitcoinapp import gp

user = 'christle' #add your username here (same as previous postgreSQL)            
host = 'localhost'
dbname = 'birth_db'
db = create_engine('postgres://%s%s/%s'%(user,host,dbname))
con = None
con = psycopg2.connect(database = dbname, user = user)


def get_ico_prediction_row(ico_name):
  dbname = 'christle'
  username = 'christle'
  pswd = gp.get_psql_password()

  engine = create_engine('postgresql://%s:%s@localhost/%s'%(username,pswd,dbname))

  # connect:
  con = None
  con = psycopg2.connect(database = dbname, user = username, host='localhost', password=pswd)
  QUERY="""SELECT * FROM icoprediction
  WHERE coinname = '{}'
  """.format(ico_name)
  query_results = pd.read_sql_query(QUERY,con)
  query_results['closed_utc'] = datetime.datetime.utcfromtimestamp(query_results['closed_utc']).strftime('%Y-%m-%d')
  return query_results

@app.route('/')
@app.route('/index', methods=['GET', 'POST'])
def index():
    #form = InputForm(request.form)
    if request.method == 'POST':
        print('Got POST method')
        ico_name_submitted = request.form['ico_form_selection']
        ico_results = get_ico_prediction_row(ico_name_submitted)
        print('ico name submitted is {}'.format(ico_name_submitted))
        print('ico results is {}'.format(ico_results))
        expert_results = pd.DataFrame()
    else:
        ico_results = pd.DataFrame()
        expert_results = pd.DataFrame()


    return render_template("index.html",
       list_of_icos = ['Opus', 'Paquarium', 'Agrello', 'Tierion', 'Blocktix', 
       'district0x Network', 'SunContract', 'FundYourselfNow', 'Blocktix', 
       'RootProject', 'TrueFlip', 'GeoFounders', 'Primalbase', 'Eros', 'SkinCoin', 
       'Gilgam', 'Gilgam.es', 'CoinDash', 'Sumerchain', 'Mothership', 'PressOne', 
       'SONM', 'Orocrypt', 'Tezos', 'InsureX', 'Nimiq', 'ATBcoin', 'LeviarCoin', 'OnPlace', 
       'Polybius', 'Santiment', 'Rialto', 'Starta', 'AdEx', 'BlockPool', 'DCORP', '21 Million', 
       'SilverCoin', 'iDice', 'Octanox', 'Wagerr', 'CryptoPing', 'NVO', 'TenX', 'MaskNetwork', 
       'OmiseGO', 'Civic', 'Status', 'Internet of Coins', 'Monaco', 'Minexcoin', 'SuperDAO', 
       'Bancor', 'Aira', 'Zrcoin', 'EcoBit', 'Cofound.it', 'VOISE', 'Patientory', 'Embermine',
        'Adel', 'Basic Attention Token', 'Exscudo', 'Mysterium Network', 'Suretly', 'MobileGo', 
        'Storj', 'E4ROW', 'Viva Coin', 'Peerplays', 'Ethbits', 'Legends Room', 'BOScoin',
         'Quantum Resistant Ledger', 'TokenCard', 'Creativechain', 'Apptrade', 'Lunyr', 
         'Back to Earth', 'TaaS', 'Gnosis', 'IEX.EC', 'WeTrust', 'Aeternity', 'Cosmos Network',
          'Matchpool', 'Equibit', 'Chain of Points', 'CashScripter', 'Qtum', 'Edgeless', 'Lykke',
           'Augmentors', 'Etheroll', 'Melon', 'Chronobank', 'Dfinity', 'Wings', 'Darcrus', 
           'BlockCDN', 'vDice', 'Ark', 'Golos', 'Beyond the Void', 'Arcade City', 'ETCWin',
            'Komodo', 'Golem', 'Decent', 'Synereo', 'Antshares', 'Metaverse', 'HEAT', 
            'Breakout Coin', 'The DAO', 'Project Decorum', 'DigixDAO', 'Lisk', 'Iota', 
            'Augur', 'Ethereum', 'Storjcoin X', 'MaidSafeCoin', 'Counterparty'],
        ico_results = ico_results
       )


@app.route('/experts')
def expert_page():
  expert_series = pd.Series([[2122, 'nullc'], [1119, 'evoorhees'], [908, 'luke-jr'],
   [774, 'Throwahoymatie'], [718, 'Introshine'], [700, 'BashCo'], [699, 'petertodd'], [664, 'pb1x'],
    [623, 'Vibr8gKiwi'], [588, 'paleh0rse'], [562, 'GibbsSamplePlatter'], [554, 'BobAlison'],
     [489, 'ferroh'], [486, 'ToTheMoonGuy'], [476, 'killerstorm'], [475, 'belcher_'], 
     [467, 'jratcliff63367'], [446, 'theymos'], [441, 'PotatoBadger'], [439, 'jmw74'],
      [438, 'cap2002'], [424, 'usrn'], [422, 'bruce_fenton'], [415, 'Cryptolution'],
       [402, 'physalisx'], [400, 'spottedmarley'], [392, 'Sugar_Daddy_Peter'],
        [386, 'maaku7'], [379, 'AnalyzerX7'], [375, 'throwaway-o'], [373, 'bitusher'], 
        [363, 'dellintelbitcoin'], [362, 'BitttBurger'], [356, 'IkmoIkmo'],
         [350, 'gavinandresen'], [348, 'Frogolocalypse'], [339, 'SeansOutpost'], 
         [337, 'rydan'], [328, 'dskloet'], [327, 'waxwing'], [326, 'xrandr'], 
         [315, 'ferretinjapan'], [311, 'kinoshitajona'], [307, 'Noosterdam'], 
         [304, 'Piper67'], [301, 'gonzobon'], [294, 'Frankeh'], [293, 'throckmortonsign'], 
         [291, 'smartfbrankings'], [289, 'pizzaface18'], [284, 'Natanael_L'], 
         [282, 'kryptomancer'], [282, 'Cowboy_Coder'], [281, 'aminok'], [281, 'thieflar'],
          [280, 'jcoinner'], [277, 'totes_meta_bot'], [273, 'AstarJoe'], [272, 'Julian702'],
           [271, 'kiisfm'], [270, 'ztsmart'], [265, 'lifeboatz'], [265, 'slowmoon'], 
           [262, 'supermari0'], [262, 'sreaka'], [261, 'TheSelfGoverned'], [257, 'riplin'], 
           [254, 'whitslack'], [254, 'Lite_Coin_Guy'], [253, 'cypherdoc2'], [253, 'Logical007'], 
           [250, 'knight222'], [249, 'eragmus'], [249, 'conv3rsion'], [249, 'Amanojack'], 
           [248, 'chrisrico'], [247, 'MyDixieWreck4BTC'], [246, 'Thorbinator'], [245, 'moral_agent'],
            [245, 'hugolp'], [245, 'muyuu'], [239, 'd4d5c4e5'], [239, 'zeusa1mighty'], 
            [238, 'btchombre'], [235, 'ebaley'], [235, 'Anenome5'], [234, 'tophernator'], 
            [233, 'chalash'], [233, 'cqm'], [233, 'trilli0nn'], [226, 'Sovereign_Curtis'], 
            [225, 'prelsidente'], [224, 'bubbasparse'], [223, 'yorrick21'], [222, '_niko'], 
            [222, 'NimbleBodhi'], [220, 'murbul'], [217, 'hardleft121'], [216, 'bitpotluck'],
             [215, 'Shibinator'], [215, 'pluribusblanks'], [214, 'nobodybelievesyou'], 
             [214, 'adam3us'], [214, 'nopara73'], [212, 'xcsler'], [212, 'elux'], 
             [212, 'pdtmeiwn'], [210, 'Dude-Lebowski'], [209, 'drcross'], [209, 'zoopz'], 
             [209, 'moleccc'], [208, 'marcus_of_augustus'], [207, 'yeh-nah-yeh'], [207, 'Essexal'], 
             [206, 'violencequalsbad'], [205, 'hairy_unicorn'], [205, 'danielravennest'], 
             [203, 'stcalvert'], [202, 'gizram84'], [201, 'digitalh3rmit'], [198, 'statoshi'],
              [198, 'pyalot'], [197, 'cpgilliard78'], [196, 'flamingboard'], [195, 'Lentil-Soup'], 
              [194, 'sgornick'], [193, 'secret_bitcoin_login'], [192, 'mike_hearn'], 
              [192, 'jonny1000'], [191, 'AnonymousRev'], [191, 'ConditionDelta'], [190, 'Lejitz'],
               [190, 'KoKansei'], [190, 'vakeraj'], [190, 'coastermonger'], [190, 'vbenes'],
                [189, 'bitcoind3'], [188, 'blackmarble'], [188, 'tsontar'], [187, 'i_can_get_you_a_toe'], 
                [185, 'mmeijeri'], [185, 'UKcoin'], [183, 'chriswheeler'], [183, 'paperraincoat'], 
                [183, 'SatoshisCat'], [183, 'dooglus'], [182, 'PoliticalDissidents'], 
                [182, 'zombiecoiner'], [181, 'Chakra_Scientist'], [181, 'cryptonaut420'], [181, 'runeks'], 
                [181, 'bbbbbubble'], [178, 'SatoshisGhost'], [178, 'kwanijml'], [176, 'GSpotAssassin'], 
                [175, 'Yoghurt114'], [174, 'Rassah'], [173, 'n0mdep'], [173, 'vbuterin'], [173, 'jgarzik'],
                 [173, 'oakpacific'], [171, 'paavokoya'], [171, 'Bitcoinopoly'], [171, 'rmvaandr'], 
                 [170, 'bitsteiner'], [170, 'stormsbrewing'], [169, 'twfry'], [168, 'BeastmodeBisky'],
                  [168, 'Aahzmundus'], [167, 'goonsack'], [165, 'wserd'], [165, 'dillpicklechips'], 
                  [163, 'Taek42'], [163, 'btcdrak'], [162, 'futilerebel'], [162, 'xygo'], 
                  [162, 'anaccountjustforyouu'], [161, 'Capt_Roger_Murdock'], [160, 'bitcointip'],
                   [160, 'notreddingit'], [159, 'sumBTC'], [158, 'chuckymcgee'], [158, 'CC_EF_JTF'], 
                   [158, 'sQtWLgK'], [158, '7trXMk6Z'], [157, 'targetpro'], [157, 'canad1andev3loper'],
                    [156, 'Cryptoconomy'], [155, 'arcrad'], [154, 'ebliever'], [153, 'giszmo'], 
                    [153, 'sqrt7744'], [153, 'jrmxrf'], [152, 'token_dave'], [152, 'andreasma'], 
                    [151, 'Yorn2'], [151, 'Anen-o-me'], [151, 'Future_Prophecy'], [151, 'handsomechandler']])

  return render_template("experts.html", expert_series = expert_series)


@app.route('/db')
def birth_page():
    sql_query = """                                                             
                SELECT * FROM birth_data_table WHERE delivery_method='Cesarean'\;                                                                               
                """
    query_results = pd.read_sql_query(sql_query,con)
    births = ""
    print(query_results[:10])
    for i in range(0,10):
        births += query_results.iloc[i]['birth_month']
        births += "<br>"
    return births

@app.route('/db_fancy')
def cesareans_page_fancy():
    sql_query = """
               SELECT index, attendant, birth_month FROM birth_data_table WHERE delivery_method='Cesarean';
                """
    query_results=pd.read_sql_query(sql_query,con)
    births = []
    for i in range(0,query_results.shape[0]):
        births.append(dict(index=query_results.iloc[i]['index'], attendant=query_results.iloc[i]['attendant'], birth_month=query_results.iloc[i]['birth_month']))
    return render_template('cesareans.html',births=births)


@app.route('/input')
def cesareans_input():
    return render_template("input.html")

@app.route('/output')
def cesareans_output():
  #pull 'birth_month' from input field and store it
  patient = request.args.get('birth_month')
    #just select the Cesareans  from the birth dtabase for the month that the user inputs
  query = "SELECT index, attendant, birth_month FROM birth_data_table WHERE delivery_method='Cesarean' AND birth_month='%s'" % patient
  print(query)
  query_results=pd.read_sql_query(query,con)
  print(query_results)
  births = []
  for i in range(0,query_results.shape[0]):
      births.append(dict(index=query_results.iloc[i]['index'], attendant=query_results.iloc[i]['attendant'], birth_month=query_results.iloc[i]['birth_month']))
  the_result = ModelIt(patient,births)
  return render_template("output.html", births = births, the_result = the_result)