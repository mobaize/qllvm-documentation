@ECHO OFF

pushd %~dp0

REM 清理之前的构建
rmdir /s /q build

REM 创建构建目录
mkdir build

REM 构建英文文档
mkdir build\en
sphinx-build -b html -D master_doc=index.en source build\en

REM 构建中文文档
mkdir build\zh_CN
sphinx-build -b html -D master_doc=index source build\zh_CN

echo 多语言文档构建完成！
echo 英文文档：build\en
echo 中文文档：build\zh_CN

popd
pause