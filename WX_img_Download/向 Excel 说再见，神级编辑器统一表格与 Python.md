## 向 Excel 说再见，神级编辑器统一表格与 Python

[Python开发者](javascript:void(0);) *昨天*

（给Python开发者加星标，提升Python技能）



> 转自：机器之心



![img](https://mmbiz.qpic.cn/mmbiz_png/KmXPKA19gW8ytVicE1O0s0Mgah7D455yDjCVspwCwkNOKxoibSctmKsJ5UtmZQvBmJ570Yv3H0pKsIUFYGUsdc7w/640?wx_fmt=png&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)



是的，在一个界面上同时展示可视化表格与代码，而且同时通过表格与代码修改数据，这不就是 Python 与 Excel 的结合吗？



项目地址：https://github.com/ricklamers/gridstudio



我们先看看 Grid studio 的效果到底是什么样的。总体而言，我们既可以通过 Python 加载和处理数据，也能通过「Excel」操作数据。



![img](https://mmbiz.qpic.cn/mmbiz_gif/KmXPKA19gW8ytVicE1O0s0Mgah7D455yDFcQVoczkWr1Y1CyWT9hVMbiaAaw2gCPpoT1oK1so42cenyRwfPjk7xw/640?wx_fmt=gif&tp=webp&wxfrom=5&wx_lazy=1)



在 Python 上处理数据比较好理解，表格上处理数据其实非常像 Excel，如下所示为写一个求和公式。



![img](https://mmbiz.qpic.cn/mmbiz_gif/KmXPKA19gW8ytVicE1O0s0Mgah7D455yD84WJic2NoeXldcia2FzrSE3nRKAZZxlWNksCYibBtohrTicOOb5kDhhkHQ/640?wx_fmt=gif&tp=webp&wxfrom=5&wx_lazy=1)



也许我们在表格上改了些数据，那么我们也能导入到 NumPy 数组，并做进一步的运算。



![img](https://mmbiz.qpic.cn/mmbiz_gif/KmXPKA19gW8ytVicE1O0s0Mgah7D455yD6fYickDfhp35Pweiahic21BNyUrOdsaxszg2BoXa1686NEcbydoYXlMEw/640?wx_fmt=gif&tp=webp&wxfrom=5&wx_lazy=1)



**为什么要创建这个工具？**



作者表示，他创建 Grid studio 主要是用来解决数据科学项目中工作流分散的问题，在这种项目中，他要在 R studio、Excel 等多个工具之间换来换去。



在为 gazillionth-time 导出 CSV 文件时，如果行数过高，应用程序窗口就会卡顿。即使是做一些简单的事情，比如读取 JSON 文件，也能把人逼疯。现有的工具无法提供高效工作所需的环境和相关工作流，这也是作者决定构建该工具的原因。他想要创建一个易用的应用程序，可以把数据科学工作流整合进去。



**这个工具有何亮点？**



Grid studio 是一个基于网页的应用，看起来和 Google Sheets、Microsoft Excel 差不多。然而，它的杀手锏是整合了 Python 语言。



几乎所有使用过计算机的人都会很自然地使用表格来查看和编辑数据。将这个简单的 UI 与 Python 这种成熟的编程语言结合起来简直不要太好用。



用 Python 编写脚本非常简单：只需编写几行代码直接运行即可。



![img](https://mmbiz.qpic.cn/mmbiz_gif/KmXPKA19gW8ytVicE1O0s0Mgah7D455yDmS6eVrZqXEKmg6WcxOtibq6OKWbniaO5uE5nhJhjlAxiaTpIRtpbEshow/640?wx_fmt=gif&tp=webp&wxfrom=5&wx_lazy=1)



**核心集成：****读、写**



这一 Python 集成的核心是对电子表格的读写接口，它可以在电子表格的数据和 Python 进程中的数据之间建立一个高性能的连接。



可以用以下方式在表格中写入数据：



```
sheet("A1:A3", [1, 2, 3])
```



用以下这种方式从表格中读取数据：



```
my_matrix = sheet("A1:A3")
```



你可以通过这种简单而高效的方式直接在表格中读取或写入数据，以自动化数据输入、提取、可视化等过程。



**编写定制化表格函数**



虽然通过一个简单的接口完成读写非常灵活，但有时编写可以直接调出的定制化函数也很重要。



除了 AVERAGE、SUM、IF 这些默认函数外，你可能还需要其他函数，那么写出来就好了！



```
def UPPERCASE(a):
    return str(a).uppercase()
```



写完这行代码后，在表格中调出该函数，就像调用常规函数一样。



**利用 Python 生态**



通过利用 Python 生态中各种强大的软件包，我们能立即访问到当前最优的数据科学工具，因此也能快速访问到强大的模型，例如线性回归和支持向量机等。



![img](https://mmbiz.qpic.cn/mmbiz_png/KmXPKA19gW8ytVicE1O0s0Mgah7D455yDCcAEyzXQRicKm0bnx2ccr7kKA4t8DwdqB3kjHvcUKVhwRowC3aJDJFQ/640?wx_fmt=png&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)



因为本身 Grid studio 主要就是处理表格数据，那么将它们作为特征可以快速调用 SVM 等模型，从而探索隐藏在这些数据背后的特征。



**数据可视化**



在数据科学中，很常见的一个任务就是可视化数据，这样才能获得关于数据的「先验知识」。通过集成交互式绘图库 Plotly.js 和 Python 标准可视化库 Matplotlib，Grid studio 目前已经内置了高级绘图功能。如下所示我们可以在向量表格格式上使用高级绘图功能：



![img](https://mmbiz.qpic.cn/mmbiz_gif/KmXPKA19gW8ytVicE1O0s0Mgah7D455yDtqbmzUFpqKKVF6VreE6MbMaKfC5GDNXwnLz66BSzyWialm2W38x9dww/640?wx_fmt=gif&tp=webp&wxfrom=5&wx_lazy=1)



为了进一步解释如何使用 Grid studio 的特征以构建可视化图标，项目作者还展示了两个案例，即爬取网页与可视化数据分布，但这里主要展示第一个案例。



案例：估计正态分布



如下案例展示了 Grid studio 的强大功能，它会以更高的保真度通过 Plotly.js 可视化正态分布，我们可以看看交互式制图到底是如何完成的。



![img](https://mmbiz.qpic.cn/mmbiz_gif/KmXPKA19gW8ytVicE1O0s0Mgah7D455yD7qkMrooAYszbiaiaJiae10sic9KspKI62Sc8WhY75pReoDe6fTkqa6Q8dw/640?wx_fmt=gif&tp=webp&wxfrom=5&wx_lazy=1)



**使用安装**



前面介绍了这么多特性，那么我们到底该怎么用呢？Grid studio 的安装和使用都非常简单，通过简单的命令行就能搞定。



- git clone https://github.com/ricklamers/gridstudio
- cd gridstudio && ./run.sh







如上通过下载项目、运行安装脚本两步，我们就能在浏览器中打开本地端口，然后就能愉快地使用了。



*参考链接：*

*https://hackernoon.com/introducing-grid-studio-a-spreadsheet-app-with-python-to-make-data-science-easier-tdup38f7**https://github.com/ricklamers/gridstudio*
*https://gridstudio.io*