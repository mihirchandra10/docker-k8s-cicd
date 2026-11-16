# Docker + Kubernetes + CI/CD

An end-to-end delivery pipeline for a small Python web service:

1. **Build**: multi-stage Docker image, running as a non-root user
2. **Test**: pytest runs on every push
3. **Publish**: image pushed to GitHub Container Registry (`ghcr.io`), tagged with the commit SHA
4. **Deploy**: Kubernetes Deployment with readiness/liveness probes, resource limits, a HorizontalPodAutoscaler and an Ingress

```
 git push ─▶ GitHub Actions ─▶ test ─▶ docker build ─▶ ghcr.io ─▶ kubectl apply ─▶ cluster
```

## Run locally

```bash
docker compose up --build
curl http://localhost:8080/healthz
```

## Deploy to Kubernetes

```bash
kubectl apply -k k8s/
kubectl -n demo get pods,svc,hpa,ingress
```

## Layout

| Path | Purpose |
|---|---|
| `app/` | Flask service (`/`, `/healthz`, `/metrics`) and tests |
| `Dockerfile` | Multi-stage build, non-root, gunicorn |
| `docker-compose.yml` | Local run |
| `k8s/` | Namespace, Deployment, Service, HPA, Ingress (Kustomize) |
| `.github/workflows/ci-cd.yml` | Test → build → push pipeline |

## Skills demonstrated

Docker · Kubernetes · Kustomize · GitHub Actions · Container security (non-root, read-only filesystem, resource limits) · Prometheus metrics endpoint
