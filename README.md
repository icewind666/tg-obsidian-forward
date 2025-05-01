## build

docker build -t tg-obsidian-forward-bot .

## run container

docker run -d \
  --name tg-obsidian-forward-bot \
  --restart unless-stopped \
  --network="host" \
  --env-file .env.docker \
  -v $(pwd):/usr/src/app/vault \
  -v $(pwd)/img:/usr/src/app/img \
  -v $(pwd)/paths.txt:/usr/src/app/paths.txt \
  tg-obsidian-forward-bot
  