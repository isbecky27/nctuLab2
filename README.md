# Network Topology with Mininet

This repository is lab for NCTU course "Introduction to Computer Networks 2018".

---
## Abstract

In this lab, we are going to write a Python program which can generate a network topology using Mininet and use iPerf to measure the bandwidth of the topology.

---
## Objectives

1. Learn how to create a network topology with Mininet
2. Learn how to measure the bandwidth in your network topology with iPerf

---
## Execution

   - 輸入指令: sudo chmod +x topology.py 和 sudo ./topology.py 執行topology.py檔
   - 若出現錯誤 如: Exception: Error creating interface pair (s1-eth1,s2eth1): RTNETLINK answers: File exist
   - 則輸入指令: sudo mn -c 將其清乾淨後重新執行 sudo ./topology.py 即可
   - 接下來進入mininet
   - 輸入iPerf指令 h6 iperf -s -u -i 1 > ./out/result & 和 h3 iperf -c 10.0.0.6 -u –i 1
   - 結果如下圖 packet loss 的機率位在13~18%間則成功
    ![image](https://github.com/nctucn/lab2-isbecky27/blob/master/result.jpg)
      
---
## Description

### Mininet API in Python

> TODO:
> * Describe the meaning of Mininet API in Python you used in detail



### iPerf Commands

Topo2.png iPref指令
'mininet> h6 iperf -s -u -i 1 > ./out/result &'
host 6 開啟iPerf 以server模式啟動 使用udp通訊協定 每隔1s更新頻寬資訊 結果result檔會傳至out資料夾中
'mininet> h3 iperf -c 10.0.0.6 -u –i 1'
host 3 開啟iPerf 以client模式啟動 並連線到IP為10.0.0.6的server(host 6) 使用udp通訊協定 每隔1s更新頻寬資訊
   - -s 以server模式啟動
   - -u 使用udp協議
   - -i 每隔多少秒更新頻寬資訊
   - -c 執行client模式啟動，並連線到server的IP

### Tasks

1. **Environment Setup**
   - 首先先載PieTTY IP位址為140.133.195.69 port為13316(學號末5碼)
   - 登入 Login:root Password:0210 (改密碼 指令:passwd)
   - 輸入指令:git clone https://github.com/nctucn/lab2-isbecky27.git Network_Topology 將檔案複製下來
   - 接著登入github Username for 'https://github.com': isbecky27 和 Password for 'https://isbecky27@github.com': 密碼
   - 試著執行 Mininet 使用指令:sudo mn 接下來若跑出錯誤訊息 如:You may wish to try "service openvswitch-switch start".
   - 則輸入指令:sudo service openvswitch-switch start 然後再執行一次 sudo mn 即可

2. **Example of Mininet**
   - 試著執行example.py 記得將路徑跳至/root/Network_Topology/src/
   - 輸入指令執行example.py:sudo chmod +x example.py 和 sudo ./example.py
   - 則會出現以下的結果
     ![image](https://github.com/nctucn/lab2-isbecky27/blob/master/example.jpg)
   - 若跳出錯誤訊息 如:Exception: Error creating interface pair (s1-eth1,s2eth1): RTNETLINK answers: File exist
   - 則輸入指令:sudo mn -c 將其清乾淨後重新執行一次即可

3. **Topology Generator**
   - 13316%3(學號末5碼%3)=2 找出自己要做的圖 topo2.png
   - 依照topo2.png的圖 寫一個檔名為topology.py的python程式(code要有註解) 並將放在和example.py同層
   - 記得code中需加入from mininet.util import dumpNodeConnections 和 dumpNodeConnections(net.hosts) 和 dumpNodeConnections(net.switches
   - 且加入CLI: from mininet.cli import CLI 和 CLI(net)
   - 再來執行topology.py: sudo ./topology.py 
   - 若跳出錯誤訊息 如:Exception: Error creating interface pair (s1-eth1,s2eth1): RTNETLINK answers: File exist
   - 則輸入指令:sudo mn -c 將其清乾淨後重新執行一次即可

4. **Measurement**
   - 用iPerf指令去測試topology.py
   - topo2.png的測試指令: mininet> h6 iperf -s -u -i 1 > ./out/result & 和 mininet> h3 iperf -c 10.0.0.6 -u –i 1
   - 執行完的packet loss的機率應介於13~18%之間
   - 最後的result會在out的資料夾裡

---
## References

* **References**
    * [Iperf頻寬測試工具@ PiNG^2 :: 隨意窩Xuite日誌](https://blog.xuite.net/u870q217/blog/31513614-Iperf%E9%A0%BB%E5%AF%AC%E6%B8%AC%E8%A9%A6%E5%B7%A5%E5%85%B7)
    * [Mininet Python API Reference Manual](http://mininet.org/api/annotated.html)
* **Mininet**
    * [Mininet Walkthrough](http://mininet.org/walkthrough/)
    * [Introduction to Mininet](https://github.com/mininet/mininet/wiki/Introduction-to-Mininet)
    * [Mininet Python API Reference Manual](http://mininet.org/api/annotated.html)
    * [A Beginner's Guide to Mininet](https://opensourceforu.com/2017/04/beginners-guide-mininet/)
    * [GitHub/OSE-Lab - 熟悉如何使用 Mininet](https://github.com/OSE-Lab/Learning-SDN/blob/master/Mininet/README.md)
    * [菸酒生的記事本 – Mininet 筆記](https://blog.laszlo.tw/?p=81)
    * [Hwchiu Learning Note – 手把手打造仿 mininet 網路](https://hwchiu.com/setup-mininet-like-environment.html)
    * [阿寬的實驗室 – Mininet 指令介紹](https://ting-kuan.blog/2017/11/09/%E3%80%90mininet%E6%8C%87%E4%BB%A4%E4%BB%8B%E7%B4%B9%E3%80%91/)
    * [Mininet 學習指南](https://www.sdnlab.com/11495.html)
* **Python**
    * [Python 2.7.15 Standard Library](https://docs.python.org/2/library/index.html)
    * [Python Tutorial - Tutorialspoint](https://www.tutorialspoint.com/python/)
* **Others**
    * [iPerf3 User Documentation](https://iperf.fr/iperf-doc.php#3doc)
    * [Cheat Sheet of Markdown Syntax](https://www.markdownguide.org/cheat-sheet)
    * [Vim Tutorial – Tutorialspoint](https://www.tutorialspoint.com/vim/index.htm)
    * [鳥哥的 Linux 私房菜 – 第九章、vim 程式編輯器](http://linux.vbird.org/linux_basic/0310vi.php)

---
## Contributors

* [Ching](https://github.com/isbecky27)
* [David Lu](https://github.com/yungshenglu)

---
## License

GNU GENERAL PUBLIC LICENSE Version 3
