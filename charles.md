# charles 使用手册
1. charles和whistle的区别
（1）charles有客户端软件，whistle是浏览器里的插件
（2）charles可以抓https的请求，whistle抓不到https的请求

3. charles配置流程
（1）https://www.charlesproxy.com/ -- 官网下载软件
（2）下载完成后安装即可使用
（3）安装证书help -- SSL Proxying -- Install Charles Root Certification -- 安装完成后，右键，显示完整信息，信任证书
（4）手机安装证书 -- 配置代理（Charles代理地址，可以在help -- local IP address查看，选择env0）
（5）配置好代理后，客户端会弹窗提示有新设备接入，选择信任即可
（6）手机接入后，浏览器输入charles.pro/ssl，下载证书并安装信任
（7）客户端打开https的抓包开关，Proxy -- SSL Proxying Settings -- SSL Proxying -- 选择enable ssl proxying，打开开关，并且在下方添加 *.* 的host和port（不配置的话，会导致抓不到https的回包，或者回包乱码）
