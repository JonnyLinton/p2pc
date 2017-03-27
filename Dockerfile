FROM python:3

ADD p2pc.py /
ADD display.py /
ADD parsing.py /
ADD sender_receiver.py /
ADD setup.py /

RUN pip install -e .

CMD [ "p2pc" ]