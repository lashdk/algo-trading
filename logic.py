# -*- coding: utf-8 -*-
"""
Created on Mon Jun  1 02:49:43 2020

@author: dhruv
"""

  
    
    
    

class Logic(object):
    def __init__(self,Technical_analysis,weights):
        self.tech_analysis=Technical_analysis
        self.weights=weights
        self.long=0
        self.short=0
        self.long_cash=None
        self.short_cash=None

    def long_call(self):
        bullish_marubozu=self.tech_analysis.bullish_marubozu()
        if bullish_marubozu[0]==True:
            self.long +=self.weights["bullish_marubozu"]
        
        bullish_hammer=self.tech_analysis.bullish_hammer()
        if bullish_hammer[0]==True:
            self.long +=self.weights["bullish_hammer"]
        
        bullish_inverted_hammer=self.tech_analysis.bullish_inverted_hammer()
        if bullish_inverted_hammer[0]==True:
            self.long +=self.weights["bullish_inverted_hammer"]
            
        
        bullish_engulfing=self.tech_analysis.bullish_engulfing()
        if bullish_engulfing[0]==True:
            self.long +=self.weights["bullish_engulfing"]
        
        bullish_piercing_pattern=self.tech_analysis.bullish_piercing_pattern()
        if bullish_piercing_pattern[0]==True:
            self.long +=self.weights["bullish_piercing_pattern"]
        
        bullish_harami=self.tech_analysis.bullish_harami()
        if bullish_harami[0]==True:
            self.long +=self.weights["bullish_harami"]
        
        bullish_morning_star=self.tech_analysis.bullish_morning_star()
        if bullish_morning_star[0]==True:
            self.long +=self.weights["bullish_morning_star"]
        
        volume=self.tech_analysis.volume()
        if volume==True:
            self.long +=self.weights["volume"]
        
        
        
        if 0.10<=self.long<=0.20:
            self.long_cash=0.05
            
        elif 0.20<self.long<=0.30:
            self.long_cash=0.06
            
        elif 0.30<self.long<=0.40:
            self.long_cash=0.07
            
        elif 0.40<self.long<=0.50:
            self.long_cash=0.08
            
        elif 0.50<self.long<=0.60:
            self.long_cash=0.09
            
        elif 0.60<self.long<=0.70:
            self.long_cash=0.10
            
        elif 0.70<self.long<=0.80:
            self.long_cash=0.11
            
        elif self.long>0.80:
            self.long_cash=0.15
        
        
        return self.long_cash
            
            
    def short_call(self):
        bearish_marubozu=self.tech_analysis.bearish_marubozu()
        if bearish_marubozu[0]==True:
            self.short +=self.weights["bearish_marubozu"]
        
        bearish_hanging_man=self.tech_analysis.bearish_hanging_man()
        if bearish_hanging_man[0]==True:
            self.short +=self.weights["bearish_hanging_man"]
        
        bearish_shooting_star=self.tech_analysis.bearish_shooting_star()
        if bearish_shooting_star[0]==True:
            self.short +=self.weights["bearish_shooting_star"]
        
        bearish_engulfing=self.tech_analysis.bearish_engulfing()
        if bearish_engulfing[0]==True:
            self.short +=self.weights["bearish_engulfing"]
        
        bearish_dark_cloud_cover=self.tech_analysis.bearish_dark_cloud_cover()
        if bearish_dark_cloud_cover[0]==True:
            self.short +=self.weights["bearish_dark_cloud_cover"]
        
        bearish_harami=self.tech_analysis.bearish_harami()
        if bearish_harami[0]==True:
            self.short +=self.weights["bearish_harami"]
        
        bearish_evening_star=self.tech_analysis.bearish_evening_star()
        if bearish_evening_star[0]==True:
            self.short +=self.weights["bearish_evening_star"]
            
        volume=self.tech_analysis.volume()
        if volume==True:
            self.short +=self.weights["volume"]
        
         
        if 0<self.short<=0.20:
            self.short_cash=0.05
            
        elif 0.20<self.short<=0.30:
            self.short_cash=0.06
            
        elif 0.30<self.short<=0.40:
            self.short_cash=0.07
            
        elif 0.40<self.short<=0.50:
            self.short_cash=0.08
            
        elif 0.50<self.short<=0.60:
            self.short_cash=0.09
            
        elif 0.60<self.short<=0.70:
            self.short_cash=0.10
            
        elif 0.70<self.short<=0.80:
            self.short_cash=0.11
            
        elif self.short>0.80:
            self.short_cash=0.15
        
        
        return self.short_cash
    
    def ema_50_100(self):
        
        ema50=self.tech_analysis.bullish_ema_50_100
        cash=0.10
        return (ema50,cash)
        