from boto.sqs import connect_to_region
from will.plugin import WillPlugin
from will.decorators import respond_to


class SQSChecker(WillPlugin):
    @respond_to("SQS (?P<queue_name>.*) (?P<region>.*)", case_sensitive=False)
    # @respond_to("SQS (?P<queue_name>.*)$")
    # @respond_to("How many messages are there in (?P<queue_name>.*)+"
    #            " region (?P<region>.*)", acl=['sqs'])
    def get_messages_in_sqs_queue(self, message,
                                  queue_name=None,
                                  region=None):
        """
        SQSBot: I can tell you how many messages are in our SQS queues.
                Usage: "@ByndieBot How many messages are there in <queue> in <region>
        """
        
        # handle default values
        if not queue_name:
            queue_name = 'image-regenerate-requests'
        
        if not region:
            region = 'eu-west-1'
        
        try:
            c = connect_to_region(region)
        except:
            self.reply(message, '"{}" is not a real region. (idiot) (idiot) (idiot)'.format(region)) 
        else:
            try:
                messages_in_queue = c.get_queue_attributes(
                    c.get_queue(queue_name))['ApproximateNumberOfMessages']
                messages_in_flight = c.get_queue_attributes(
                    c.get_queue(queue_name))['ApproximateNumberOfMessagesNotVisible']
            except:
                self.reply(message, '"{}" is not a real queue. (idiot) (idiot) (idiot)'.format(queue_name)) 
            else:
                self.reply(message,
                           "There are ~{} messages ({} in flight) in the {} queue in {}"
                           .format(messages_in_queue, messages_in_flight,
                                   queue_name, region))
