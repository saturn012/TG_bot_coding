const express = require('express');
const { TelegramClient } = require('telegram');
const { StringSession } = require('telegram/sessions');
const { Api } = require('telegram');
require('dotenv').config();

const app = express();
const port = 3005; // можешь изменить порт

const apiId = parseInt(process.env.API_ID);
const apiHash = process.env.API_HASH;
const stringSession = new StringSession(process.env.SESSION);


app.get('/get-messages', async (req, res) => {
  const channelUsername = req.query.channel;
  const limit = parseInt(req.query.limit || '10');
  const offsetId = parseInt(req.query.offsetId || '0');
  const offsetFromNewest = req.query.offsetFromNewest === 'true';
  const offsetDateParam = req.query.offsetDate; // новое!

  if (!channelUsername) {
    return res.status(400).json({ error: 'channel parameter is required' });
  }

  try {
    const client = new TelegramClient(stringSession, apiId, apiHash, {
      connectionRetries: 5,
    });

    await client.start();

    const dialogs = await client.getDialogs();
    const found = dialogs.find(
      (dialog) =>
        dialog.entity.className === 'Channel' &&
        (dialog.entity.username === channelUsername ||
         dialog.entity.id.toString() === channelUsername)
    );

    if (!found) {
      return res.status(404).json({ error: 'Channel not found in your dialog list. Make sure you are subscribed to it.' });
    }

    const entity = found.entity;

    const options = {
      limit,
    };

    if (offsetId > 0) {
      options.offsetId = offsetId;
    }

    // ✅ Добавим фильтрацию по дате, если передана
    if (offsetDateParam) {
      const parsedDate = new Date(offsetDateParam);
      if (isNaN(parsedDate.getTime())) {
        return res.status(400).json({ error: 'Invalid offsetDate format. Use YYYY-MM-DD or ISO string.' });
      }

      // Telegram API принимает offsetDate как объект Date
      options.offsetDate = Math.floor(parsedDate.getTime() / 1000); // в секундах
    }

    const messages = await client.getMessages(entity, options);

    const result = messages.map(msg => ({
      id: msg.id,
      text: msg.message,
      date: msg.date,
      senderId: msg.senderId,
      views: msg.views,
      forwards: msg.forwards,
      media: msg.media ? true : false,
    }));

    await client.disconnect();

    return res.json({
      messages: result,
      nextOffsetId: messages.length > 0 ? messages[messages.length - 1].id : null,
    });
  } catch (err) {
    console.error('Ошибка при получении сообщений:', err);
    return res.status(500).json({ error: err.message });
  }
});






app.get('/get-channels', async (req, res) => {
  try {
    const client = new TelegramClient(stringSession, apiId, apiHash, {
      connectionRetries: 5,
    });

    await client.start();

    const dialogs = await client.getDialogs();

    const channels = dialogs
      .filter(dialog => dialog.entity.className === 'Channel')
      .map(dialog => ({
        id: dialog.entity.id,
        accessHash: dialog.entity.accessHash,
        title: dialog.entity.title,
      }));

    await client.disconnect();

    return res.json(channels);
  } catch (err) {
    console.error('Ошибка при получении каналов:', err.message);
    return res.status(500).json({ error: err.message });
  }
});




app.listen(port, () => {
    
  console.log(`Telegram API сервер запущен на http://localhost:${port}`);
});
