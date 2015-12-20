'''
Script for detecting 3rd party Ad libraries.

buzzcity --> Remaining.
'''

import subprocess, os

class AdLibraryDetection:
    def __init__(self, scan_id, decompiled_app_path):
        self.library_list = []
        self.apk_name = "Box_2.1.1.apk"
        self.smali_path = os.path.join(decompiled_app_path, 'smali')
        self.scan_id = scan_id

    def detect(self):
        self.adlib_list = []
        paths = [x[0] for x in os.walk(self.smali_path)]
        for path in paths:
            adlib = str(path).split(self.smali_path)[1]
            adlib = adlib.split("/")
            adlib = ".".join(adlib)
            self.adlib_list.append(adlib)
        return self.adlib_list

        
    # def detect(self):
    #     print "Detect function called"
    #     if os.path.isdir(self.smali_path + 'com/google/ads'):
    #         self.library_list.append('AdMob')

    #     if os.path.isdir(self.smali_path + 'com/flurry'):
    #         self.library_list.append('Flurry')

    #     if os.path.isdir(self.smali_path + 'com/inmobi'):
    #         self.library_list.append('InMobi')

    #     if os.path.isdir(self.smali_path + 'com/tapjoy'):
    #         self.library_list.append('TapJoy')

    #     if os.path.isdir(self.smali_path + 'com/mobclix'):
    #         self.library_list.append('MobClix')

    #     if os.path.isdir(self.smali_path + 'com/chartboost'):
    #         self.library_list.append('ChartBoost ')

    #     if os.path.isdir(self.smali_path + 'com/adwhirl'):
    #         self.library_list.append('AdWhirl')

    #     if os.path.isdir(self.smali_path + 'com/mopub'):
    #         self.library_list.append('MoPub')

    #     if os.path.isdir(self.smali_path + 'com/greystripe'):
    #         self.library_list.append('GreyStripe')

    #     if os.path.isdir(self.smali_path + 'com/jumptap'):
    #         self.library_list.append('Jumptap')

    #     if os.path.isdir(self.smali_path + 'com/google/analytics'):
    #         self.library_list.append('Google Analytics')

    #     if os.path.isdir(self.smali_path + 'com/admob'):
    #         self.library_list.append('AdMob')

    #     if os.path.isdir(self.smali_path + 'com/burstly'):
    #         self.library_list.append('Burstly')

    #     if os.path.isdir(self.smali_path + 'com/sponsorpay'):
    #         self.library_list.append('SponsorPay')

    #     if os.path.isdir(self.smali_path + 'com/cauly'):
    #         self.library_list.append('Cauly')

    #     if os.path.isdir(self.smali_path + 'com/mobfox'):
    #         self.library_list.append('MobFox')

    #     if os.path.isdir(self.smali_path + 'com/vpon'):
    #         self.library_list.append('Vpon')

    #     if os.path.isdir(self.smali_path + 'com/appbrain'):
    #         self.library_list.append('AppBrain')

    #     if os.path.isdir(self.smali_path + 'net/daum'):
    #         self.library_list.append('Daum')

    #     if os.path.isdir(self.smali_path + 'com/admarvel'):
    #         self.library_list.append('AdMarvel')

    #     if os.path.isdir(self.smali_path + 'com/applovin'):
    #         self.library_list.append('AppLovin')

    #     if os.path.isdir(self.smali_path + 'com/adfonic'):
    #         self.library_list.append('Adfonic')

    #     if os.path.isdir(self.smali_path + 'com/getjar'):
    #         self.library_list.append('GetJar')

    #     if os.path.isdir(self.smali_path + 'com/nexage'):
    #         self.library_list.append('NexAge')

    #     if os.path.isdir(self.smali_path + 'com/inneractive'):
    #         self.library_list.append('InnerActive')

    #     if os.path.isdir(self.smali_path + 'com/pontiflex'):
    #         self.library_list.append('Pontiflex')

    #     if os.path.isdir(self.smali_path + 'com/zestadz'):
    #         self.library_list.append('ZestAdz')

    #     if os.path.isdir(self.smali_path + 'com/madhouse'):
    #         self.library_list.append('MadHouse')

    #     if os.path.isdir(self.smali_path + 'com/smaato'):
    #         self.library_list.append('Smaato')

    #     if os.path.isdir(self.smali_path + 'net/youmi'):
    #         self.library_list.append('YouMi')

    #     if os.path.isdir(self.smali_path + 'de/madvertise'):
    #         self.library_list.append('mAdvertise')

    #     if os.path.isdir(self.smali_path + 'cn/domob'):
    #         self.library_list.append('DoMob')

    #     if os.path.isdir(self.smali_path + 'com/jirbo/adcolony'):
    #         self.library_list.append('Jirbo/AdColony')

    #     if os.path.isdir(self.smali_path + 'com/revmob'):
    #         self.library_list.append('RevMob')

    #     if os.path.isdir(self.smali_path + 'com/senddroid'):
    #         self.library_list.append('SendDroid')

    #     if os.path.isdir(self.smali_path + 'com/airpush'):
    #         self.library_list.append('AirPush')

    #     if os.path.isdir(self.smali_path + 'com/tapit'):
    #         self.library_list.append('Tapit')

    #     if os.path.isdir(self.smali_path + 'com/medialets'):
    #         self.library_list.append('Medialets')
    #     if os.path.isdir(self.smali_path + 'mediba/ad'):
    #         self.library_list.append('Mediba')
    #     if os.path.isdir(self.smali_path + 'com/papaya'):
    #         self.library_list.append('Papaya')

    #     if os.path.isdir(self.smali_path + 'com/huntmads'):
    #         self.library_list.append('Hunt Mobile Ads')

    #     if os.path.isdir(self.smali_path + 'com/rhythmnewmedia'):
    #         self.library_list.append('RhythmNewMedia')

    #     if os.path.isdir(self.smali_path + 'com/tapfortap'):
    #         self.library_list.append('TapForTap')

    #     if os.path.isdir(self.smali_path + 'com/adknowledge'):
    #         self.library_list.append('AdKnowledge')
    #     if os.path.isdir(self.smali_path + 'net/metaps'):
    #         self.library_list.append('Metaps')
    #     if os.path.isdir(self.smali_path + 'com/wiyun'):
    #         self.library_list.append('WiYun')
    #     if os.path.isdir(self.smali_path + 'com/vdopia'):
    #         self.library_list.append('Vdopia')
    #     if os.path.isdir(self.smali_path + 'com/waps'):
    #         self.library_list.append('Waps')
    #     if os.path.isdir(self.smali_path + 'com/adwo'):
    #         self.library_list.append('AdWo')
    #     if os.path.isdir(self.smali_path + 'com/mobosquare'):
    #         self.library_list.append('MoboSquare')

    #     if os.path.isdir(self.smali_path + 'mobi/vserv'):
    #         self.library_list.append('Vserv')

    #     if os.path.isdir(self.smali_path + 'com/wooboo'):
    #         self.library_list.append('WooBoo')
    #     if os.path.isdir(self.smali_path + 'com/everbadge'):
    #         self.library_list.append('EverBadge')
    #     if os.path.isdir(self.smali_path + 'com/mt/airad'):
    #         self.library_list.append('AirAd')
    #     if os.path.isdir(self.smali_path + 'com/noqoush/adfalcon'):
    #         self.library_list.append('AdFalcon')
    #     if os.path.isdir(self.smali_path + 'com/moolah'):
    #         self.library_list.append('Moolah')
    #     if os.path.isdir(self.smali_path + 'com/kuguo'):
    #         self.library_list.append('Kuguo')
    #     if os.path.isdir(self.smali_path + 'com/adsmogo'):
    #         self.library_list.append('AdSmogo')
    #     if os.path.isdir(self.smali_path + 'com/sellaring'):
    #         self.library_list.append('SellAring')
    #     if os.path.isdir(self.smali_path + 'com/startapp'):
    #         self.library_list.append('StartApp')


    #     if os.path.isdir(self.smali_path + 'com/admoda'):
    #         self.library_list.append('AdModa')

    #     if os.path.isdir(self.smali_path + 'com/mobpartner'):
    #         self.library_list.append('MobPartner')
    #     if os.path.isdir(self.smali_path + 'com/quclix'):
    #         self.library_list.append('Quclix')
    #     if os.path.isdir(self.smali_path + 'com/ldevelop'):
    #         self.library_list.append('LDevelop')


    #     for item in self.library_list:
    #         print item
if __name__ == "__main__":
    obj = AdLibraryDetection()
    obj.detect()


