from WMCore.Configuration import Configuration
config = Configuration()
config.section_("General")
config.General.requestName   = 'BulkGravWW700-vN'
config.General.transferLogs = True

config.section_("JobType")
config.JobType.pluginName  = 'Analysis'
config.JobType.inputFiles = ['Spring16_25nsV10_MC_L1FastJet_AK4PFchs.txt','Spring16_25nsV10_MC_L2Relative_AK4PFchs.txt','Spring16_25nsV10_MC_L3Absolute_AK4PFchs.txt','Spring16_25nsV10_MC_L1FastJet_AK8PFchs.txt','Spring16_25nsV10_MC_L2Relative_AK8PFchs.txt','Spring16_25nsV10_MC_L3Absolute_AK8PFchs.txt','Spring16_25nsV10_MC_L1FastJet_AK8PFPuppi.txt','Spring16_25nsV10_MC_L2Relative_AK8PFPuppi.txt','Spring16_25nsV10_MC_L3Absolute_AK8PFPuppi.txt']
# Name of the CMSSW configuration file
#config.JobType.psetName    = 'bkg_ana.py'
config.JobType.psetName    = 'analysis.py'
#config.JobType.allowUndistributedCMSSW = True
config.JobType.allowUndistributedCMSSW = True

config.section_("Data")
#config.Data.inputDataset = '/WJetsToLNu_13TeV-madgraph-pythia8-tauola/Phys14DR-PU20bx25_PHYS14_25_V1-v1/MINIAODSIM'
config.Data.inputDataset = '/BulkWWlvqq-700N-v1/qili-MiniAODv2-A-9c82be0544462ee57448ab37ee74ae1a/USER'
#config.Data.inputDBS = 'global'
config.Data.inputDBS = 'phys03'
config.Data.splitting = 'FileBased'
config.Data.unitsPerJob =1 
config.Data.totalUnits = -1
config.Data.publication = False
config.Data.allowNonValidInputDataset = True

# This string is used to construct the output dataset name
config.Data.outputDatasetTag = 'BulkGravWW700'

config.section_("Site")
# Where the output files will be transmitted to
config.Site.storageSite = 'T2_CH_CERN'
