# from prometheus_client import Counter, Histogram, generate_latest, CONTENT_TYPE_LATEST
# from fastapi import FastAPI, Request, Response
# from starlette.middleware.base import BaseHTTPMiddleware
# import time

# REQUEST_COUNT= Counter('http_request_total', "Total HTTP Requests", ['method', 'endpoint', 'status'])
# REQUEST_LATENCY= Histogram("http_request_duration_seconds", "HTTP Request Latency", ['method', 'endpoint'])


# class PrometheusMiddleware(BaseHTTPMiddleware):
    
#     async def dispatch(self, request: Request, call_next):
        
#         start_time = time.time()
        
#         # Process the request
#         response= await call_next(request)
        
#         # Record metrics after request is processed
#         duration = time.time() - start_time
#         endpoint = request.url.path            # get endpoint name
        
#         REQUEST_LATENCY.labels(method=request.method, endpoint=endpoint).observe(duration)
#         REQUEST_COUNT.labels(method=request.method, endpoint=endpoint, status=response.status_code).inc()
        
#         return response

# def setup_metrics(app: FastAPI):
#     """
#     Setup Prometheus metrics middleware and endpoint
#     """
#     # Add Prometheus middleware
#     app.add_middleware(PrometheusMiddleware)

#     @app.get("/TrhBVe_m5gg2002_E5VVqS", include_in_schema=False)
#     def metrics():
#         return Response(generate_latest(), media_type=CONTENT_TYPE_LATEST)
    
    
from prometheus_client import Counter, Histogram, generate_latest, CONTENT_TYPE_LATEST
from fastapi import FastAPI, Request, Response
from starlette.middleware.base import BaseHTTPMiddleware
import time

REQUEST_COUNT = Counter('http_request_total', "Total HTTP Requests", ['method', 'endpoint', 'status'])
REQUEST_LATENCY = Histogram("http_request_duration_seconds", "HTTP Request Latency", ['method', 'endpoint'])

# Define the metrics endpoint path
METRICS_ENDPOINT = "/TrhBVe_m5gg2002_E5VVqS"

# Endpoints to exclude from metrics tracking (monitoring/health check endpoints)
EXCLUDED_PATHS = {
    METRICS_ENDPOINT,
    "/openapi.json",
    "/health",
    "/ready",
    "/favicon.ico"  # Also exclude favicon requests
}


class PrometheusMiddleware(BaseHTTPMiddleware):
    
    async def dispatch(self, request: Request, call_next):
        start_time = time.time()
        
        # Process the request
        response = await call_next(request)
        
        # Skip recording metrics for excluded endpoints
        endpoint = request.url.path
        if endpoint in EXCLUDED_PATHS:
            return response
        
        # Record metrics after request is processed
        duration = time.time() - start_time
        
        # Add logging to debug unexpected requests
        import logging
        logger = logging.getLogger(__name__)
        logger.info(f"Recording metric: {request.method} {endpoint} - Status: {response.status_code} - Duration: {duration:.4f}s - Client: {request.client.host if request.client else 'unknown'}")
        
        REQUEST_LATENCY.labels(method=request.method, endpoint=endpoint).observe(duration)
        REQUEST_COUNT.labels(method=request.method, endpoint=endpoint, status=response.status_code).inc()
        
        return response


def setup_metrics(app: FastAPI):
    """
    Setup Prometheus metrics middleware and endpoint
    """
    # Add Prometheus middleware
    app.add_middleware(PrometheusMiddleware)

    @app.get(METRICS_ENDPOINT, include_in_schema=False)
    def metrics():
        return Response(generate_latest(), media_type=CONTENT_TYPE_LATEST)