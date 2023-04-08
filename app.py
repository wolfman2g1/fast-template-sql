from fastapi import FastAPI
import uvicorn
import logging
import logging.config
from service.logging_config import LOGGING_CONFIG
from fastapi.middleware.cors import CORSMiddleware
from opentelemetry import trace
from opentelemetry.instrumentation.fastapi import FastAPIInstrumentor
from service.settings import config



"Log setup"
logging.config.dictConfig(LOGGING_CONFIG)
logger = logging.getLogger(__name__)

# Acquire a tracer
tracer = trace.get_tracer(__name__)
# Acquire a meter.
meter = metrics.get_meter(__name__)

def configure_app():
    logger.info("Using Config %s", config.ENV)
    app = FastAPI(docs_url="/api/v1/docs")
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"]
    )
   # app.include_router(ping.router)
    app.include_router(customer.router)
    app.include_router(contacts.router)
    app.include_router(techs.router)

    return app
FastAPIInstrumentor.instrument_app(app)

if __name__ == "__main__":
    logger.info(f"Starting {config.SERVICE_NAME}")
    app = configure_app()
    uvicorn.run(app, host="0.0.0.0")