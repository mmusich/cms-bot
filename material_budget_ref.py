MATERIAL_BUDGET_REF = {
  "CMSSW_8_1_X" : "CMSSW_8_1_X_2017-03-12-0000",
  "CMSSW_9_0_X" : "CMSSW_9_0_X_2017-03-14-1100",
  "CMSSW_9_1_X" : "CMSSW_9_0_X_2017-03-14-1100",
  "CMSSW_9_2_X" : "CMSSW_9_0_X_2017-03-14-1100",
  "CMSSW_9_3_X" : "CMSSW_9_0_X_2017-03-14-1100",
  "CMSSW_9_4_X" : "CMSSW_9_0_X_2017-03-14-1100", 
  "CMSSW_10_0_X" : "CMSSW_9_0_X_2017-03-14-1100",
}

def get_ref():
  from os import environ
  print MATERIAL_BUDGET_REF["_".join(environ['CMSSW_VERSION'].split("_")[0:3])+"_X"]
