#!/usr/bin/python
# RFTap test functions
# Dec 2016, alex.farrant@contextis.co.uk

import socket

def rftapUDP(freq,nfreq,pwr,noise,snr,dur,lat,lon,alt,bw,rxgain):
	s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	s.sendto(rftapPacket(freq,nfreq,pwr,noise,snr,dur,lat,lon,alt,bw,rxgain), (server,1664))
	s.close()

def rftapPacket(freq,nfreq,pwr,noise,snr,dur,lat,lon,alt,bw,rxgain):
	flag1=254
	flag2=254 # location, duration, time (unix), 
	rt=time.time() # NOW
	time1Packed = struct.pack('d',int(rt))
	time2Packed = struct.pack('d',rt-int(rt))
	freqPacked = struct.pack('d',freq)
	nfreqPacked = struct.pack('d',nfreq)
	offsetPacked = struct.pack('d',freq-nfreq)
	durPacked = struct.pack('d',dur)
	powerPacked = struct.pack('f',pwr)
	noisePacked = struct.pack('f',noise)
	snrPacked = struct.pack('f',snr)
	latPacked = struct.pack('d',lat)
	lonPacked = struct.pack('d',lon)
	altPacked = struct.pack('d',alt)
	bwPacked = struct.pack('f',bw)
	rxgPacked = struct.pack('f',rxgain)
	magic="52467461" # 'RFTa'
	body="%02x%02x" % (flag1,flag2) \
		+"%s" % (freqPacked.encode("hex")) \
		+"%s" % (nfreqPacked.encode("hex")) \
		+"%s" % (offsetPacked.encode("hex")) \
		+"%s" % (powerPacked.encode("hex")) \
		+"%s" % (noisePacked.encode("hex")) \
		+"%s" % (snrPacked.encode("hex")) \
		+"%s" % (time1Packed.encode("hex")) \
		+"%s" % (time2Packed.encode("hex")) \
		+"%s" % (durPacked.encode("hex")) \
		+"%s" % (latPacked.encode("hex")) \
		+"%s" % (lonPacked.encode("hex")) \
		+"%s" % (altPacked.encode("hex")) \
		+"%s" % (bwPacked.encode("hex")) \
		+"%s" % (rxgPacked.encode("hex"))
	rftapLen = "%02x00" % (int((len(body)/2)+6)/4) # num of 4byte words in payload + options
	body=magic+rftapLen+body
	return body.decode("hex") 


