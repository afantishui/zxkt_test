function download()
{	Set-ExecutionPolicy UnRestricted
	$client = new-object System.Net.WebClient
	$client.DownloadFile("http://niubo.oss-cn-shenzhen.aliyuncs.com/live/client/nsb-teacher-1.0.3.0-dev.exe", "E:\\zxkt\\nsb-teacher-1.0.3.0-dev.exe")
}
 


