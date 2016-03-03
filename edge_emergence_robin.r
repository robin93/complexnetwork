#setting the working directory to the folder which contains the code
this.dir <- dirname(parent.frame(2)$ofile)
setwd(this.dir)

#http://www.biostat.jhsph.edu/~rpeng/docs/R-large-tables.html
#read the data file; using colClasses to improve the efficiency of the file reading process
tab5rows <- read.table("MItoMI-2013-11-03.txt",sep='\t',header = FALSE, nrows = 5)
classes <- sapply(tab5rows, class)
rawdata <- read.table("MItoMI-2013-11-03.txt", sep='\t',nrows = 10000,header = FALSE, colClasses = classes)

names(rawdata)<-c('Timestamp', 'Source_GridLoc', 'Destination_GridLoc', 'Strength_factor')
#rawdata$Timestamp2= sapply(rawdata$Timestamp,function(x){format(as.POSIXct(x, origin="1970-01-01", tz="CET"), '%H')})
#rawdata <- rawdata[,-1]
#rawdata

#edgestrength_by_timestamp <- aggregate(rawdata[!(rawdata$Source_GridLoc ==rawdata$Destination_GridLoc), ]$Strength_factor, list(rawdata[!(rawdata$Source_GridLoc ==rawdata$Destination_GridLoc), ]$Timestamp2),sum)
edgestrength_by_timestamp <- by(rawdata$Strength_factor, list(rawdata$Timestamp),sum)
names(edgestrength_by_timestamp) <- c('Timestamp','Sum_of_edge_strength')
edgestrength_by_timestamp

#write the output to csv
write.csv(edgestrength_by_timestamp, file = "edgestrength_by_timestamp.csv",row.names=FALSE)

