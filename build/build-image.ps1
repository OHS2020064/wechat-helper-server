param([string]$dir='\GitHub',[string]$img_version='v1.0.0',[int]$e=0,[string]$img_name='bot-server')
docker login --username=ohsaly --password=lgb2536807 registry.cn-shanghai.aliyuncs.com
if($e-eq1)
{
Copy-Item $dir'\build\Dockerfile-Environment' $dir'\Dockerfile'
docker build -t $img_name-environment:v1.0.0 .
}
Copy-Item $dir'\build\Dockerfile-Executable' $dir'\Dockerfile'
docker build -t $img_name-executable:$img_version .
docker tag $img_name-executable:$img_version registry.cn-shanghai.aliyuncs.com/ohs-sys-stage/$img_name-executable:$img_version
docker push registry.cn-shanghai.aliyuncs.com/ohs-sys-stage/$img_name-executable:$img_version
