# supermemo-hanization

软件：passolo2022、python

可能需要的dll：32位SQLite.Interop.dll，放到软件根目录即可。
可能需要的文件；sm19.01.exe、sm18.chs（懒人包）

汉化后生成的chs文件仅对源文件生效。所以考虑如何重用项目汉化后的资源是比较重要的事情。

- sm18cs.glo supermemo18懒人包的术语文件
- .glo术语文件采用的文本编码为UTF-16 LE。TAB制表符分割。可以用Excel打开去重。
- script1.py 对比passolo导出的文本格式生成术语文件的预处理文件。
- sm19c.lpu 19.01的汉化项目。
- sm19c-1.lpu 19.01导入sm18cs.glo术语文件后的汉化项目 50%的汉化进度。
- sm18cs.lpu 18.05  懒人包sm18.chs文件解析后生成的汉化项目。
- ZH-CN.tra 对比替换懒人包的对应字段。tra文件要在SuperMemo软件设置中设置后使用。


汉化重用方式：

1. 术语表预翻译。
2. 扫描目标文件(校准)翻译
3. ...待探索。
