from array import *
import argparse

# python massjobs.py -g FSCEPonly

argParser = argparse.ArgumentParser()
argParser.add_argument("-g", "--geometry", help="geometry code")

args = argParser.parse_args()
print("args=%s" % args)

print("args.name=%s" % args.geometry)

# Check your working area
basedir="/cms/data/hatake/ana/CalVision/DD4hep_102b/DD4hep/"

# Various directories
compactdir=basedir+"/examples/DualTestBeam/compact/"
outputarea=basedir+"/examples/DualTestBeam/compact/output/"
hostarea=basedir+"/examples/DualTestBeam/compact/jobs/"

# Directions & position
#direction="0 0.176 1."
#position="0.,0*mm,-1*cm"
direction="0 0.05 0.99875"
position="0.,-7*mm,-1*cm"

# LCG setup script
LCGsetup="/cvmfs/sft.cern.ch/lcg/views/LCG_102b/x86_64-centos8-gcc11-opt/setup.sh"

nenergy=10
energies=[10,15,20,25,30,35,40,45,50,100]
name="pbs-executable-"+args.geometry+"-dial-"

# create the .sh files for electrons
i=0
while (i<nenergy):
    print(i)
    shfile = open(hostarea+name+str(energies[i])+'_GeV-e.sh',"w")

    shfile.write('#!/bin/bash'+'\n')
    shfile.write('cd '+compactdir+'\n')
    shfile.write('START_TIME=`/bin/date`'+'\n')
    shfile.write('echo "started at $START_TIME"'+'\n')
    shfile.write('echo "started at $START_TIME on ${HOSTNAME}"'+'\n')
    shfile.write('source '+LCGsetup+'\n')
    shfile.write('echo "ran setup"'+'\n')
    shfile.write('source  '+basedir+'/install/bin/thisdd4hep.sh'+'\n')
    shfile.write('module load gl_fix' + '\n')
    shfile.write('echo "ran thisdd4hep"'+'\n')
# another good direction is  "0 0.05 0.99875"  and position 0.,-7*mm,-1*cm use this for pure fiber
# DO IT BOTH PLACES!!!
#    shfile.write('ddsim --compactFile=/cms/data/truitta/dd4hep/DD4hep/examples/DualTestBeam/compact/DR'+args.geometry+'.xml --runType=batch -G --steeringFile /cms/data/truitta/dd4hep/DD4hep/examples/DualTestBeam/compact/SCEPCALsteering.py --outputFile='+outputarea+'out_'+args.geometry+'-dial_'+str(energies[i])+'GeV_e-.root --part.userParticleHandler='' -G --gun.position="0.,0*mm,-1*cm" --gun.direction "0 0.0 1." --gun.energy "'+str(energies[i])+'*GeV" --gun.particle="e-" -N 500 >& '+outputarea+'sce_e_'+args.geometry+'-dial_'+str(energies[i])+'.log'+'\n')
    shfile.write('ddsim --compactFile='+compactdir+'/DR'+args.geometry+'.xml --runType=batch -G --steeringFile '+compactdir+'/SCEPCALsteering.py --outputFile='+outputarea+'/out_'+args.geometry+'-dial_'+str(energies[i])+'GeV_e-.${PBS_ARRAY_INDEX}.root --part.userParticleHandler='' -G --gun.position="'+position+'" --gun.direction "'+direction+'" --gun.energy "'+str(energies[i])+'*GeV" --gun.particle="e-" -N 50 >& '+outputarea+'sce_e_'+args.geometry+'-dial_'+str(energies[i])+'.${PBS_ARRAY_INDEX}.log'+'\n')
    shfile.write('exitcode=$?'+'\n')
    shfile.write('echo ""'+'\n')
    shfile.write('END_TIME=`/bin/date`'+'\n')
    shfile.write('echo "finished at $END_TIME"'+'\n')
    shfile.write('exit $exitcode'+'\n')

    shfile.close()
    i=i+1
    print("file closed")

# create the .sh files for pions
i=0
while (i<nenergy):
    print(i)
    shfile = open(hostarea+name+str(energies[i])+'_GeV-pi.sh',"w")

    shfile.write('#!/bin/bash'+'\n')
    shfile.write('cd '+compactdir+'\n')
    shfile.write('START_TIME=`/bin/date`'+'\n')
    shfile.write('echo "started at $START_TIME"'+'\n')
    shfile.write('echo "started at $START_TIME on ${HOSTNAME}"'+'\n')
    shfile.write('source '+LCGsetup+'\n')
    shfile.write('echo "ran setup"'+'\n')
    shfile.write('source  '+basedir+'/install/bin/thisdd4hep.sh'+'\n')
    shfile.write('echo "ran thisdd4hep"'+'\n')
    #shfile.write('ddsim --compactFile=/cms/data/hatake/ana/CalVision/DD4hep_102b/DD4hep/examples/DualTestBeam/compact/DR'+args.geometry+'.xml --runType=batch -G --steeringFile /cms/data/hatake/ana/CalVision/DD4hep_102b/DD4hep/examples/DualTestBeam/compact/SCEPCALsteering.py --outputFile='+outputarea+'out_'+args.geometry+'-dial_'+str(energies[i])+'GeV_pi-.${PBS_ARRAY_INDEX}.root --part.userParticleHandler='' -G --gun.position="0.,0*mm,-1*cm" --gun.direction "0 0.176 1." --gun.energy "'+str(energies[i])+'*GeV" --gun.particle="pi-" -N 50 >& '+outputarea+'sce_pi_'+args.geometry+'-dial_'+str(energies[i])+'.${PBS_ARRAY_INDEX}.log'+'\n')
    shfile.write('ddsim --compactFile='+compactdir+'/DR'+args.geometry+'.xml --runType=batch -G --steeringFile '+compactdir+'/SCEPCALsteering.py --outputFile='+outputarea+'out_'+args.geometry+'-dial_'+str(energies[i])+'GeV_pi-.${PBS_ARRAY_INDEX}.root --part.userParticleHandler='' -G --gun.position="'+position+'" --gun.direction "'+direction+'" --gun.energy "'+str(energies[i])+'*GeV" --gun.particle="pi-" -N 50 >& '+outputarea+'sce_pi_'+args.geometry+'-dial_'+str(energies[i])+'.${PBS_ARRAY_INDEX}.log'+'\n')
    shfile.write('exitcode=$?'+'\n')
    shfile.write('echo ""'+'\n')
    shfile.write('END_TIME=`/bin/date`'+'\n')
    shfile.write('echo "finished at $END_TIME"'+'\n')
    shfile.write('exit $exitcode'+'\n')

    shfile.close()
    i=i+1
    print("file closed")


# create the .jdl files for electrons
# i=0
# while (i<nenergy):
#     print(i)
#     jdlfile = open(hostarea+name+str(energies[i])+'-e.jdl',"w")
#     jdlfile.write("universe = vanilla"+'\n')
#     jdlfile.write("Executable ="+hostarea+name+str(energies[i])+"_GeV-e.sh"+'\n')
#     jdlfile.write("should_transfer_files = NO"+'\n')
#     jdlfile.write("Requirements = TARGET.FileSystemDomain == \"privnet\""+'\n')
#     jdlfile.write("Output = "+hostarea+name+str(energies[i])+"-e_sce_$(cluster)_$(process).stdout"+'\n')
#     jdlfile.write("Error = "+hostarea+name+str(energies[i])+"-e_sce_$(cluster)_$(process).stderr"+'\n')
#     jdlfile.write("Log = "+hostarea+name+str(energies[i])+"-e_sce_$(cluster)_$(process).condor"+'\n')
#     jdlfile.write("Arguments = SCE"+'\n')
#     jdlfile.write("Queue 1"+'\n')
#     jdlfile.close()
#     i=i+1
#     print("file closed")

# create the .jdl files for pins
# i=0
# while (i<nenergy):
#     print(i)
#     jdlfile = open(hostarea+name+str(energies[i])+'-pi.jdl',"w")
#     jdlfile.write("universe = vanilla"+'\n')
#     jdlfile.write("Executable ="+hostarea+name+str(energies[i])+"_GeV-pi.sh"+'\n')
#     jdlfile.write("should_transfer_files = NO"+'\n')
#     jdlfile.write("Requirements = TARGET.FileSystemDomain == \"privnet\""+'\n')
#     jdlfile.write("Output = "+hostarea+name+str(energies[i])+"-pi_sce_$(cluster)_$(process).stdout"+'\n')
#     jdlfile.write("Error = "+hostarea+name+str(energies[i])+"-pi_sce_$(cluster)_$(process).stderr"+'\n')
#     jdlfile.write("Log = "+hostarea+name+str(energies[i])+"-pi_sce_$(cluster)_$(process).condor"+'\n')
#     jdlfile.write("Arguments = SCE"+'\n')
#     jdlfile.write("Queue 1"+'\n')
#     jdlfile.close()
#     i=i+1
#     print("file closed")

# create the submitter file
# f = open("massjobs.sh",'w')
# f.write('chmod 777 '+hostarea+'*'+'\n')
# i=0
# while (i<nenergy):
#     f.write("condor_submit "+hostarea+name+str(energies[i])+'-e.jdl'+'\n')
#     f.write("condor_submit "+hostarea+name+str(energies[i])+'-pi.jdl'+'\n')
#     i=i+1
# f.write("condor_q")
# f.close()



