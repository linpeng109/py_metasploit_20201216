from pymetasploit3.msfrpc import MsfRpcClient

# 配置rpc的用户名和密码
client = MsfRpcClient(server='192.168.1.112', username='msf', password='msf', port=55552)
# 加载arp扫描模块，获取ip地址范围中存活主机
exploit = client.modules.use(mtype='auxiliary', mname='scanner/discovery/arp_sweep')
exploit['RHOSTS'] = '192.168.1.100-200'
# 设置进程数
exploit['THREADS'] = 5
# 超时设置
exploit['TIMEOUT'] = 5
# 获取控制台id
console_id = client.consoles.console().cid
# 执行扫描脚本
result = client.consoles.console(console_id).run_module_with_output(exploit)
print(result)
