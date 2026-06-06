def generate_logger(logger_name):
    log_dir: Path = Path("logs"),
    log_name: str = f"{logger_name}",
    console_level: int = logging.INFO,
    file_level: int = logging.DEBUG,
) -> None:

    log_dir.mkdir(parents=True, exist_ok=True)
    log_path = log_dir / log_name

    # Avoid duplicate handlers if called multiple times
    root = logging.getLogger()
    if root.handlers:
        return

    root.setLevel(logging.DEBUG)  # root collects everything; handlers filter

    # Console handler
    ch = logging.StreamHandler()
    ch.setLevel(console_level)
    ch.setFormatter(logging.Formatter(
        fmt="%(asctime)s | %(levelname)-8s | %(name)s | %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    ))

    # Rotating file handler
    fh = RotatingFileHandler(
        log_path,
        maxBytes=5_000_000,  # ~5 MB
        backupCount=3,
        encoding="utf-8",
    )
    fh.setLevel(file_level)
    fh.setFormatter(logging.Formatter(
        fmt="%(asctime)s | %(levelname)-8s | %(name)s | %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    ))

    root.addHandler(ch)
    root.addHandler(fh)
