#!/usr/bin/env bash
docker run -t -i -h OrderSystem --restart=always --name OrderSystem -d -p 9003:8000 -v /DockerRepository/AllSales/allSales:/allSales ordersystem_python
