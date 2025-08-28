const mineflayer = require('mineflayer');

function createBot() {
  const bot = mineflayer.createBot({
    host: 'ramadhansipaling.aternos.me',
    port: 48224,
    username: process.env.MC_USERNAME || 'AFKBot',
    // For premium (Microsoft) accounts, set MC_PASSWORD and auth: 'microsoft'
    password: process.env.MC_PASSWORD,
    auth: process.env.MC_AUTH || 'offline',
  });

  bot.on('login', () => {
    console.log('Bot connected to server');
  });

  bot.on('end', () => {
    console.log('Bot disconnected. Reconnecting in 10 seconds...');
    setTimeout(createBot, 10000);
  });

  bot.on('error', (err) => {
    console.error('Bot error:', err);
  });
}

createBot();
