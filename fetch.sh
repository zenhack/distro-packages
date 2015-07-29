set -e
cd "$(dirname $0)/SOURCES"
wget -i ../fetch-list
cd ..
sha512sum -c sha512sums.txt
