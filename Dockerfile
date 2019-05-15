FROM python:2.7.15

WORKDIR /common_dashboard
ENV PATH /common_dashboard:$PATH

RUN pip install dash \
                dash_core_components \
                dash_html_components \
                flask \
                gunicorn
COPY . .
EXPOSE 3001

CMD [ "gunicorn", "--bind", "0.0.0.0:3001", "common_dashboard:server" ]
