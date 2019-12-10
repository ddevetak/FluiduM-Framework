import glob



f = glob.glob("./JOBS/job-*/pion/spectra*")


print "number of files = ", len(f)
