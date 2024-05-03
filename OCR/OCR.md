baidu方案
优点：速度快，效率高，准确率高，需要联网
缺点：收费（测试接口是高精度通用文字识别：500次/天免费，还有很多其他的接口方式提供），需要注册，申请KEY
https://cloud.baidu.com/product/ocr/general

google方案
优点：免费，无需联网，可修改性强
缺点：速度慢，识别率低
https://github.com/rmtheis/tess-two

（1）Google Cloud Vision API
Google Cloud Vision API是一个功能强大的OCR工具，可以识别印刷和手写文本。它支持多种语言，并提供了高精度的文本识别结果。此外，Google Cloud Vision API还具有面部、物体和场景等其他图像识别功能。尽管这是一个强大的API，但它需要付费使用。
（2）Tesseract OCR引擎
Tesseract OCR引擎是一个开源的OCR引擎，由Google和HP共同开发。它可以将图片中的文字转换成可编辑的文本，支持多种语言。Tesseract OCR引擎在识别印刷体和手写体方面表现良好，但可能需要针对特定场景进行训练和优化。
（3）Microsoft Azure Cognitive Services
Microsoft Azure Cognitive Services提供了一系列AI服务，包括OCR功能。该服务可以快速准确地从图片中提取文本信息，支持多种语言。与其他API相比，Azure Cognitive Services提供了更广泛的定制选项和更高的准确性。然而，它也是付费使用的。


市面上有许多免费的OCR图片文字识别接口可供选择，其中比较知名的包括Google Cloud Vision API、Microsoft Azure Cognitive Services和Amazon Textract
Google Cloud Vision API是一个基于云的图像识别服务，可以识别出图片中的文字、人脸、物体等。它支持多种语言，包括中文，并且可以处理各种不同的字体和字号。使用该接口需要先在Google Cloud Platform上创建一个账号，并创建一个Vision API项目。然后，可以通过调用API来上传图片并获取识别结果。

Microsoft Azure Cognitive Services中的Computer Vision API也提供了OCR功能。它支持多种语言和字体，包括手写字体和艺术字体。使用该接口需要先在Azure Portal上创建一个Cognitive Services资源，并获取API密钥。然后，可以通过调用API来上传图片并获取识别结果。

Amazon Textract是Amazon Web Services提供的一项OCR服务。它支持多种语言和文件格式，包括PDF和图像文件。使用该接口需要先在AWS Management Console上创建一个Amazon Textract资源，并获取API密钥。然后，可以通过调用API来上传图片并获取识别结果。


除了免费的OCR接口外，市面上还有许多收费的OCR接口可供选择。这些接口通常具有更高的识别准确率和更丰富的功能，适用于对性能和准确性要求较高的场景。
其中比较知名的收费OCR接口包括Adobe Acrobat、ABBYY FineReader和Omnipage等。这些软件提供了更加强大的OCR功能，支持更多的语言和字体，并且可以处理更加复杂的场景，如手写字体、印刷质量较差的字体等。使用这些软件需要购买相应的许可证，并在个人电脑上安装相应的软件。


Tesseract，一款由HP实验室开发由Google维护的开源OCR（Optical Character Recognition , 光学字符识别）引擎，特点是开源，免费，支持多语言，多平台。

目前常用的几个OCR开源的项目
第一名：PaddleOCR
开源地址： https://github.com/PaddlePaddle/PaddleOCR.git
官网地址： https://www.paddlepaddle.org.cn/

第二名：Tesseract
Tesseract 一款由HP实验室开发由Google维护的开源OCR引擎，支持多语言，多平台，使用python开发。
开源地址： https://github.com/tesseract-oc

第三名：EasyOCR
EasyOCR是用Python编写基于Tesseract的OCR识别库，用于图像识别输出文本，目前支持80多种语言。
开源地址： https://github.com/JaidedAI/Eas


Tesseract和EasyOCR是两个常用的文字识别OCR开源框架，它们各有优势。


20个最好的免费和付费的OCR（光学字符识别）软件
https://marketsplash.com/best-free-and-paid-ocr-software/