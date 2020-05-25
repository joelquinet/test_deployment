import socket
import datetime
import module

def get_datetime_now_as_string():
    return "%s-%s-%s_%s-%s-%s" % ( str( datetime.datetime.now().year ),
                             str( datetime.datetime.now().month ).zfill( 2 ),
                             str( datetime.datetime.now().day ).zfill( 2 ),
                             str( datetime.datetime.now().hour ).zfill( 2 ),
                             str( datetime.datetime.now().minute ).zfill( 2 ),
                             str( datetime.datetime.now().second ).zfill( 2 ) )

print ('Start of the script')
while(1):
    print ('%s \t Hostname : %s \t module version : %s' % (get_datetime_now_as_string() , socket.gethostname(), module.__version__))
print ('Stop of the script')
print ('FINI')