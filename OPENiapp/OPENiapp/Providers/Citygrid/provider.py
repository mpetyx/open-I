import socket
import urllib, urllib2

class citygridplaces(object):
  	 
    def srchplaceswhere(self,what,type,where,page,rpp,sort,rformat,placement,hasoffers,histograms,i,publishercode):
        qStr = {'publisher':publishercode, 'sort':sort, 'page':page, 'rpp':rpp}
        url = "http://api.citygridmedia.com/content/places/v2/search/where?"
         
        if len(what) > 0:
            qStr['what'] = what
        if len(type) > 0:
            qStr['type'] = type
        if len(where) > 0:
            qStr['where'] = where

        if len(placement) > 0:
            qStr['placement'] = placement
        if len(hasoffers) > 0: 
            qStr['has_offers'] = hasoffers
        if len(histograms) > 0: 
            qStr['histograms'] = histograms

        if len(i) > 0: 
            qStr['i'] = i

        qStr['format'] = rformat

        url += urllib.urlencode(qStr)

        response = urllib2.urlopen( url ).read()

        return response   		

    def placesdetail(self,id,id_type,phone,customer_only,all_results,review_count,placement,format,callback,i,publishercode):

        ip = socket.gethostbyaddr(socket.gethostname())
        client_ip = str(ip[2][0])	

        qStr = {'id':id, 'id_type':id_type, 'format':format, 'publisher':publishercode, 'client_ip':client_ip}

        url = "http://api.citygridmedia.com/content/places/v2/detail?"

        if len(placement) > 0: 
            qStr['placement'] = placement
        if len(phone) > 0: 
            qStr['phone'] = phone
        if len(customer_only) > 0: 
            qStr['customer_only'] = customer_only

        if len(all_results) > 0: 
            qStr['all_results'] = all_results
        if len(review_count) > 0: 
            qStr['review_count'] = review_count
        if len(callback) > 0: 
            qStr['callback'] = callback

        if len(i) > 0: 
            qStr['i'] = i

        url += urllib.urlencode(qStr)	   	

        response = urllib2.urlopen( url ).read()

        return response   

    def placesdetail(self,id,id_type,phone,customer_only,all_results,review_count,placement,format,callback,i,publishercode):

        ip = socket.gethostbyaddr(socket.gethostname())
        client_ip = str(ip[2][0])	

        qStr = {'id':id, 'id_type':id_type, 'format':format, 'publisher':publishercode, 'client_ip':client_ip}

        url = "http://api.citygridmedia.com/content/places/v2/detail?"

        if len(placement) > 0: 
            qStr['placement'] = placement
        if len(phone) > 0: 
            qStr['phone'] = phone
        if len(customer_only) > 0: 
            qStr['customer_only'] = customer_only

        if len(all_results) > 0: 
            qStr['all_results'] = all_results
        if len(review_count) > 0: 
            qStr['review_count'] = review_count
        if len(callback) > 0: 
            qStr['callback'] = callback

        if len(i) > 0: 
            qStr['i'] = i

        url += urllib.urlencode(qStr)	   	

        response = urllib2.urlopen( url ).read()

        return response  		