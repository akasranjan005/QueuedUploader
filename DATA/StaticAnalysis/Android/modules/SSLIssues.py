#!usr/bin/python
import config
import subprocess,os
import sys
import xml.etree.ElementTree as ET
import loc_brokenTM, loc_brokenHV, loc_brokenSSF
import loc_brokenAH, loc_brokenSSE


class SSLIssues:
	def __init__(self, app_path, scan_id):
		self.app_path = app_path
		self._tm_cnt = 0
		self._hv_cnt = 0
		self._sf_cnt = 0
		self._se_cnt = 0
		self.ssl_dict = {}
		self.scan_id = scan_id

	def _getXml(self):
		print self.app_path
		cmd = ['python', config.mallodroid_script, '-f', self.app_path, '-x'] #-Later on take apk name from config file.
		output = ''
		try:
			output = subprocess.check_output(cmd)
		except Exception as e:
			print str(e)
		
		#-fetch the xml from 'output'
		if "App requires INTERNET permission." in output:
			inx_xml = output.index('<?xml version="1.0" ?>')
			self.req_output = output[inx_xml: ] #-Getting the required xml 
			self.root = ET.fromstring(self.req_output) 
			return True
		else:
			print "No INTERNET permission found. No need to worry about SSL related issues"
			return False

	def _brokenTrustManager(self):
		self.tm_dict = {}
		temp = 0
		tm_flag = 0
		for _tm in self.root.iter("trustmanager"):
			if _tm.tag != "": #- trustmanager tag present
				try:

					if _tm.attrib['broken'] == 'True':
						temp = temp + 1
						temp_dict = {}
						temp_dict['tm_class'] = _tm.attrib['class']   

						xref = _tm.find('xref')
						#print xref.attrib['class'], "---", xref.attrib['method']
						temp_dict['ref_class'] = xref.attrib['class'] 
						temp_dict['ref_method'] = xref.attrib['method']
						tm_flag += 1
						self.tm_dict[temp] = temp_dict

					else:
						print "trustmanager not broken"
				except:
					print "No attributes found for TrustManager"
			else:
				print "No TrustManager Implementation Found"
		if tm_flag != 0:
			loc_brokenTM.locBrokenTM(self.tm_dict, self.scan_id)
		return self.tm_dict


	def _brokenHostnameVerifiers(self):
		temp = 0
		self.hv_dict = {}
		hv_flag = 0
		for _hv in self.root.iter("hostnameverifier"):
			if _hv.tag != "":
				try :
					if _hv.attrib['broken'] == 'True' :
						temp = temp + 1
						temp_dict = {}
						
						temp_dict['hv_class'] = _hv.attrib['class']   

						xref = _hv.find('xref')
						#print xref.attrib['class'], "---", xref.attrib['method']
						temp_dict['ref_class'] = xref.attrib['class'] 
						temp_dict['ref_method'] = xref.attrib['method']
						hv_flag += 1
						self.hv_dict[temp] = temp_dict
					else:
						print "hostnameverifier not broken"
				except :
					print " No attributes found for hostnameverifier"
				
			else:
				print "No Hostname Verifier Implementation Found"
		if hv_flag != 0:
			loc_brokenHV.locBrokenHV(self.hv_dict, self.scan_id)
			pass
		return self.hv_dict

	def _sslFactoryImplementation(self):
		temp = 0
		self.sf_dict = {}
		ssl_f_flag = 0 
		for _sf in self.root.iter("insecuresslsocket"):
			if _sf.tag != "":
				try:
					if _sf.attrib['broken'] == 'True' :
						temp = temp + 1
						temp_dict = {}
						
						temp_dict['sf_class'] = _sf.attrib['class']   

						xref = _sf.find('xref')
						#print xref.attrib['class'], "---", xref.attrib['method']
						temp_dict['ref_class'] = xref.attrib['class'] 
						temp_dict['ref_method'] = xref.attrib['method']
						ssl_f_flag += 1
						self.sf_dict[temp] = temp_dict
					else:
						print "ssLFactory Implementation not broken"
				except :
					print "No attributes found for SSLFactory Implementation"
			else:
				print "No Hostname Verifier Implementation Found"
		if ssl_f_flag != 0:
			loc_brokenSSF.locBrokenSSF(self.sf_dict, self.scan_id)
		return self.sf_dict

	def _allowHostnameVerifier(self):
		temp = 0
		self.ah_dict = {}
		ah_flag = 0 
		for _ah in self.root.iter("allowhostnames"):
			if _ah.tag != "":
				try:
					if _ah.attrib['broken'] == 'True' :
						temp = temp + 1
						temp_dict = {}
						temp_dict['ah_class'] = _ah.attrib['class']   

						xref = _ah.find('xref')
						#print xref.attrib['class'], "---", xref.attrib['method']
						temp_dict['ref_class'] = xref.attrib['class'] 
						temp_dict['ref_method'] = xref.attrib['method']
						ah_flag += 1
						self.ah_dict[temp] = temp_dict
					else:
						print "allowHostnameVerifiers not broken"
				except Exception as e:
					print "No attributes found for allowHostnameVerifiers"
					print e
			else:
				print "No allowHostname Verifier Implementation Found"
		if ah_flag != 0:
			loc_brokenAH.locBrokenAH(self.ah_dict, self.scan_id)	
		return self.ah_dict

	def _sslError(self):
		temp = 0
		self.se_dict = {}
		sslerror_flag = 0
		for _se in self.root.iter("sslerror"):
			if _se.tag != "":
				try:
					if _se.attrib['broken'] == 'True':
						temp = temp + 1
						#self._se_dict = "_se_dict_"+str(temp)
						temp_dict = {} 
						temp_dict['se_class'] = _se.attrib['class']   
						xref = _se.find('xref')
						#print xref.attrib['class'], "---", xref.attrib['method']
						temp_dict['ref_class'] = xref.attrib['class'] 
						temp_dict['ref_method'] = xref.attrib['method']
						sslerror_flag += 1
						self.se_dict[temp] = temp_dict
					else:
						print "SSL not broken"
				except :
					print "No attributes found for sslError"
			else:
				print "No SSL Implementation Found"

		if sslerror_flag != 0:
			loc_brokenSSE.locBrokenSSE(self.se_dict, self.scan_id)

		return self.se_dict

if __name__ == '__main__':
	if len(sys.argv) <= 1:
		print "correct syntax : python SslIssues.py <apk-name>"
		sys.exit()
	else:
		apk_name = sys.argv[1]
		obj = SSLIssues(apk_name,37)
		obj._brokenTrustManager()
		# obj._brokenHostnameVerifiers()
		# obj._sslFactoryImplementation()
		# #obj._allowHostnameVerifier()
		# obj._sslError()
	