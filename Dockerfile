FROM python:3

ADD p2pc.py /
ADD display.py /
ADD parsing.py /
ADD sender_receiver.py /
ADD setup.py /
ADD sender_commands.py /
ADD semaphore.py /
ADD receiver_commands.py /
ADD channels.py /
ADD current_channel.py /

RUN pip install -e .

CMD [ "p2pc" ]