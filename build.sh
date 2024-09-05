echo "Building Vinotes CLI..."

command cd vinotes

echo "Creating Python Virtual Env"
command python -m venv venv

command source ./venv/bin/activate

echo "Installing Essential Packages"
command pip install poetry

echo "Building Package"
command poetry build

echo "Build Successful"
