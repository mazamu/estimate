 # 快速配置

1.装mysql数据库,并配置

backServer/backServer/settings

```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'testvocab',
        'USER':'test',
        'PASSWORD':'123456789',
        'HOST':'127.0.0.1',
        "PORT":'3306'
    }
}
```

 2.前端中html中ajax使用的url ip地址改为backserver实际运行的地址和端口

例如backServer运行在127.0.0.1:8000

那么就把 frontServer/templates 中出现

http://42.193.148.6:8000/ 改成http://42.193.148.6:8000/

3.启动backServer 和frontServer

backServer 为django 运行命令（可能要指定端口和ip，自行查看文档）：python manage.py runserver 

frontServer为flask 运行命令（同上）：flask_client.py

# **完成情况**

已实现基本功能：

1、 收集中考、高考、四六级、考研、雅思词汇列表等不同辅助数据，设计了一种用户词汇量估算算法

2、 设计验证方法

3、 界面设计

4、 后台批处理测试

5、 界面实例测试

额外实现功能（扩展功能）：

**1、客户端服务端架构**

**前后端分离：**

项目设计主体使用了前后端分离的思想

​    前端HTML页面通过AJAX调用后端的RESTFUL API接口并使用JSON数据进行交互。

​    Web服务器：本项目中使用flask，性能高，使用简便，用于传输html文件；

应用服务器：本项目使用django，企业级web框架，安全性，规范性高，接收/发送来自前端的json数据；

**2、数据库存储使用者数据**

使用数据库存储使用者的学号，姓名，四六级成绩，测试结果，测试时间，数据更新时间



**学生自评主要亮点**：

​    界面采用的是动态以及音乐结合的卡通形式，整体上让测试的用户在测试过程中有视觉和听觉上的享受，不至于太过枯燥乏味，尤其在小朋友群体来说是非常适合推广的。

​     功能中添加了背单词这一功能，分为音乐模式和非音乐模式，对于一部分认为记单词是一件无聊的用户群体来说是一个很不错的记忆方式。

**学生自评主要缺陷**：

安全性不佳，几乎没有安全措施，容易被人攻击。并发能力不强，每个用户进入网页后都会直接进行数据库操作，没有做缓存处理，在高并发的环境下可能会因为数据库负载高而崩溃

# 一、课程设计目的

本课程设计从解决相关应用领域实际工程问题出发进行综合实践，提高学生对软件工程发展的认识，强化学生软件能力训练，使得学生能够熟练使用专业知识和编程能力解决具体实际问题，完成软件项目的开发工作。学生通过团队合作应用软件知识开发一个具有实际工程应用背景的软件系统或解决实际工程应用背景的问题，进一步培养学生对软件工程中的需求分析等、系统分析、系统实现、软件测试的能力，掌握系统分析、系统设计、系统实现、系统维护等方法，加深学生对软件工程等相关课程的理解，增强对所选择的应用领域相关知识的认知，同时也进一步提高学生解决实际应用问题的工程综合运用能力。

# 二、课程设计内容

**设计题目**：

按照软件工程思路设计  英语词汇量估算工具；

**提交内容**：

数据（如词汇表等）、算法思路、具体设计文档（报告）、代码等；

有实际创新加分

有扩展功能加分

分组责任参考（1-8人）：

**总体设计**；

算法设计（主要是词汇量测试算法和验证方法）；

前端选择和UI设计（web、桌面程序、app、小程序等都可以）。

简单数据库选择和设计；（不限定数据库）

演示测试：两种测试，一个GUI演示测试，一个是后台批处理测试。

报告撰写。 报告必须注明成员工作量分配（总和100%，如果5个人工作量一样的话就都是20%）

**主要功能**：

收集词汇列表等不同辅助数据，设计一至多种用户词汇量估算算法；

设计验证方法： 即 衡量你的算法， 估算出来的词汇量到底有多准确？

可与业内产品做比较比如：

http://testyourvocab.com/  （首选）

百词斩词汇测试

扇贝单次词汇测试

**界面设计**：

可用web页面、桌面程序、app、小程序等。

后台批处理测试结果

可考虑 输入一个单词列表，直接算法后台计算结果

输入列表格式：词A， 认识； 词B，认识； 词C， 不认识；词D， 不认识；.... 。

输出结果：估算词汇量 

**界面实例测试结果**

找不同学生，报告测试结果 

主要数据：学号姓名（如有隐私考虑代号）、四级成绩、六级成绩、测试时间、测试结果。

**扩展功能**：

辅助数据和估算算法程序可以根据不同考虑放在服务器端或者客户端；

可用服务器端的数据、算法更新客户端相应的数据、算法；

发送学生测试实例结果到服务器端数据库 

**主要数据**：

学号姓名（如有隐私考虑代号）、四级成绩、六级成绩、测试时间、测试结果。



**其他更复杂的改进**，例如：

同一服务不同客户端的交互（比如web和app端）

不同用户的交互（例如：单词对战）

# **三、项目环境要求**

1、硬件需求:普通PC

2、软件需求:系统：Windows系统或linux系统（Ubuntu）

3、开发工具：不限

4、开发语言：不限

# **四、功能算法设计（模块设计、估计算法、评价方法）**

**模块设计：**

**1、客户端服务端架构**

 

**前后端分离****：**

项目设计主体使用了前后端分离的思想

​    前端HTML页面通过AJAX调用后端的RESTFUL API接口并使用JSON数据进行交互。

​    Web服务器：本项目中使用flask，性能高，使用简便，用于传输html文件；

应用服务器：本项目使用django，企业级web框架，安全性，规范性高，接收/发送来自前端的json数据；

**2、数据库存储使用者数据**

使用数据库存储使用者的学号，姓名，四六级成绩，测试结果，测试时间，数据更新时间

| 字段     | 含义     | 类型        | 备注              |
| -------- | -------- | ----------- | ----------------- |
| id       | 状态码   | Int(11)     | 自增主键          |
| sid      | 用户学号 | Varchar(11) |                   |
| username | 用户名   | Varchar(11) |                   |
| cet4     | 四级成绩 | Int(11)     | 必填，范围在0~750 |
| cet6     | 六级成绩 | Int(11)     | 必填，范围在0~750 |

**算法步骤：**

1. 出题环节：每一次词汇测试，系统会根据不同难度层次的词库中按照一定的比率随机抽取，在呈现在用户交互界面之前需要对抽取出来的题目随机打乱顺序；

2. 测试环节：用户开始答题，答题后将答卷传回后端

3. 答卷统计环节：

1） 后台获取用户的答卷，选出用户答对的词汇；

2） 将答对的单词分类，即比对该词库属于哪一个层次，并统计每一层次的正确率；

3） 我们设易层次单词权重为*w**1*,中层次权重为*w**2*，高层次权重为*w**3*且*w**1* + *w**2* + *w**3* =1,易层次正确率为*r**1**，*中层次正确率为*r**2**，*高层次正确率为*r**3*

4） 计算平均正确率 r = *w**1* * *r**1*+ *w**2 \** *r**2* + *w**3 \** *r**3* *，*随后用平均正确率乘以总词库数量，得到预估的词汇量

**评价方法：**

语言词汇的定量测试首要的工作就是选取一个恰当的词汇库， 不是语言中的所有词汇都可以作为测试样例。 除此之外， 还要参考国内外的研究者的一些研究成果相结合， 以及一个区域的教学水和教学习惯相结合。 选择语言词汇库的方法目前常用的有两种， 一种是词典法；另一种是使用词汇频率表法。 词汇频率表是依据词频表选择一定频率的词来测试。通常情况下，人会先记住使用频率高的词汇，人们对低频率词汇的使用少，所有不容易记住。 这就是语言词汇频率对学习者的学习影响的一个因素，对不同使用频率的词汇有着明显的差别。

我们选择语言词汇库的方法是词典法。

我们用于估算词汇量算法的词库有8000个词，词库有三种类型：四六级、考研、雅思，出题的时候按权重从三个词库抽取一定的单词，四六0.25，考研0.15，雅思0.6，这样构成了一套测试题目。

最可靠的情况下，出8000道题，测出来的结果是较为准确的；

出5000道题，测出来的结果也很接近；

出2000道题，测出来的效果也接近；

1000、900、800、700、600、500、400.....

直到找到一个效果好题目数量也不多的值，这个值就作为题数。



**结果讨论：**

   在我们的构想中，我们这款产品名叫厘米单词，因为我们主要功能是测量词汇量，所以使用了尺子作为吉祥物。我们的产品是打算面向全年龄的，因此我们采用了比较卡通的设计，因为考虑到在中小学生人群中的推广。而我们也加入了更符合人们操作习惯的“词汇速通”模式，在我们原本的设想中，点击“懂”会跳到下一个单词，点击“不懂”会弹出中文翻译提示，这样用户可以使用我们的产品来背单词。但是由于我们的英语数据太杂了，不够标准，因此中文翻译信息参差不齐，如果以后有更标准的语料库，这将是我们改进的方向。另外由于界面都是我们小组内的非专业人员绘制的，所以略显稚嫩，由于工期紧张，还没有颜色，制作更精良的界面，也是一个我们应该考虑的改进方向。
