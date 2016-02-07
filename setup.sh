## install git
cd /usr/ports/devel/git
make install

## install go
curl -Lk https://storage.googleapis.com/golang/go1.5.3.freebsd-amd64.tar.gz
tar -C /usr/local -xzf go1.5.3.freebsd-amd64.tar.gz
export PATH=$PATH:/usr/local/go/bin

## install java
cd /usr/ports/java/openjdk8
make install clean

# install python
cd /usr/ports/lang/python35
make install

# install python
cd /usr/ports/lang/ruby23
make install

# install node
cd /usr/ports/www/node
make install clean

# install julia
git clone git://github.com/JuliaLang/julia.git
git checkout release-0.4
make
ln -s julia /usr/local/bin/julia