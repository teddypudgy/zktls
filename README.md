# zkTLS Twitter AI Agent

An autonomous AI agent that promotes and educates about zkTLS technology through Twitter, making complex cryptographic concepts accessible to both technical and non-technical audiences.

## Features

- Autonomous content generation about zkTLS
- Multi-audience support (technical and general)
- Technical accuracy with engaging delivery
- Real-time interaction capabilities
- Learning and adaptation from community feedback

## Setup

1. Clone the repository:
```bash
git clone https://github.com/yourusername/zkTLS-twitter-agent.git
cd zkTLS-twitter-agent
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Set up environment variables:
```bash
cp .env.example .env
# Edit .env with your API keys
```

4. Run tests:
```bash
pytest
```

## Usage

```python
from src.agent.bot import ZkTLSAgent

# Initialize agent
agent = ZkTLSAgent()

# Generate technical content
technical_tweets = agent.generate_content(
    topic="How zkTLS improves upon traditional TLS",
    audience_type="technical"
)

# Generate general content
general_tweets = agent.generate_content(
    topic="Why zkTLS matters for online privacy",
    audience_type="general"
)
```

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details. 