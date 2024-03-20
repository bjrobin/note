Installing Geth
https://geth.ethereum.org/docs/getting-started/installing-geth#install-on-macos-via-homebrew


brew -v
# 因为以太坊客户端涉及到多个依赖安装，故先tap再安装
brew tap ethereum/ethereum
brew install ethereum
# 可通过参数--devel直接安装开发版本(可选)
brew install ethereum --devel
geth --help

# 安装完成后，可执行命令geth version查看版本信息，结果如下：
    geth version
    Geth
    Version: 1.13.14-stable
    Architecture: amd64
    Go Version: go1.22.0
    Operating System: darwin
    GOPATH=
    GOROOT=



brew update
brew upgrade
brew reinstall ethereum