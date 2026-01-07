import json
from kafka import KafkaProducer


class NewsCrawlerPipeline:
    def __init__(self):
        self.producer = KafkaProducer(
            bootstrap_servers=['localhost:9092'],
            value_serializer=lambda v:json.dumps(v, ensure_ascii=False).encode('utf-8')

        )
        self.topic = 'gold-news'

    def process_item(self, item, spider):
        try:
            self.producer.send(self.topic, item)
            self.producer.flush()
            spider.logger.info.error(f'Successfully sent item to Kafka topic {item['title'][:20]}...')
        except Exception as e:
               spider.logger.error(f'Failed to send item to Kafka: {e}')
        
        return item
    
    def close_spider(self, spider):
         self.producer.close()
         