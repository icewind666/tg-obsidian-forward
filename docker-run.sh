docker run -d \
  --name tg-obsidian-forward-bot \
  --restart unless-stopped \
  --network="host" \
  --env-file .env.docker \
  -v /Users/steelrat/icewind666-obsidian:/usr/src/app/vault \
  -v /Users/steelrat/icewind666-obsidian/img:/usr/src/app/img \
  -v $(pwd)/paths.txt:/usr/src/app/paths.txt \
  tg-obsidian-forward-bot
  