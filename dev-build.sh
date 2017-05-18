echo -e "\e[32m[+] Building the image\e[0m"
docker-compose build --no-cache &&
echo -e "\e[32m[+] Creating and launching the container.\e[0m"
docker-compose up -d
