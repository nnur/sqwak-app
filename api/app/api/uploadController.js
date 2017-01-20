const uploadController = require('express').Router();
const formidable = require('formidable');
const path = require('path');
const fs = require('fs');
const featureExtractor = require('./../services/featureExtractor');

uploadController.get('/', (req, res) => {
    res.render('upload')
});

uploadController.post('/', function(req, res){
  const form = new formidable.IncomingForm();
  form.multiples = true;
  form.uploadDir = path.join(__dirname, '/../uploads');

  const readStream = fs.createReadStream(path.join(__dirname, './../uploads/audio.wav'));
  const writeStream = featureExtractor.extract((featureVector) => {
    res.send(featureVector);
  });
  form.onPart = function(part) {
    if (!part.filename) {
        // let formidable handle all non-file parts
        form.handlePart(part);
        return;
    }
    part.on('data', (chunk) => {
        writeStream.write({ data: new Uint8Array(chunk) });
    });
    part.on('end', () => {
      writeStream.end();
    });
    part.on('error', function(err) {
        // handle this too
    });
  }

  form.parse(req);
});



module.exports = uploadController;