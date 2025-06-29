# TODO List for Toto Fonts

## Immediate Priority (Critical Fixes)

- [ ] Fix Python 2/3 compatibility issue in merge_noto.py:943 (replace `unicode()` with proper string handling)
- [ ] Create requirements.txt with dependencies (fonttools, pyyaml, nototools)
- [ ] Add basic error handling to prevent silent failures in merge scripts
- [ ] Fix hardcoded paths in shell scripts to use relative paths
- [ ] Add file existence checks before processing fonts

## Short Term (Code Quality)

- [ ] Replace print statements with proper logging using Python logging module
- [ ] Add command-line argument validation to all scripts
- [ ] Create .github/workflows/test.yml for basic CI
- [ ] Add type hints to Python functions
- [ ] Replace string path operations with pathlib
- [ ] Add progress indicators for merge operations
- [ ] Create pytest test suite with basic tests
- [ ] Add flake8 configuration and fix linting issues

## Medium Term (Architecture)

- [ ] Extract font merging logic into separate module
- [ ] Create config.yaml for centralized configuration
- [ ] Implement proper exception handling with meaningful error messages
- [ ] Add setup.py for pip installation
- [ ] Create Dockerfile for containerized deployment
- [ ] Refactor duplicate code in merge scripts
- [ ] Add font validation before and after merging
- [ ] Implement proper logging with configurable levels

## Long Term (Features)

- [ ] Create web interface using Flask/FastAPI
- [ ] Add font subsetting options to reduce file size
- [ ] Implement parallel processing for batch operations
- [ ] Create pre-merged font releases on GitHub
- [ ] Add comprehensive documentation with Sphinx
- [ ] Implement font optimization features
- [ ] Create npm package for web developers
- [ ] Add metadata preservation and reporting

## Documentation

- [ ] Update README.md with installation instructions
- [ ] Add usage examples for all scripts
- [ ] Create CONTRIBUTING.md with development guidelines
- [ ] Document Python version requirements (3.8+)
- [ ] Add troubleshooting section to README
- [ ] Create API documentation for library usage
- [ ] Add inline code comments and docstrings
- [ ] Create architecture documentation

## Testing

- [ ] Set up pytest framework
- [ ] Add unit tests for merge_fonts.py
- [ ] Add unit tests for merge_noto.py
- [ ] Add integration tests for complete workflows
- [ ] Create test fixtures with sample fonts
- [ ] Add GitHub Actions for automated testing
- [ ] Implement code coverage reporting
- [ ] Add performance benchmarks

## DevOps

- [ ] Create GitHub Actions workflow for CI/CD
- [ ] Set up automated releases
- [ ] Add security scanning with pip-audit
- [ ] Implement automated dependency updates
- [ ] Create release automation script
- [ ] Add code quality badges to README
- [ ] Set up issue templates
- [ ] Configure Dependabot

## User Experience

- [ ] Create quick start guide
- [ ] Add --help documentation to all scripts
- [ ] Improve error messages with solutions
- [ ] Create example YAML configurations
- [ ] Add verbose mode to all operations
- [ ] Create FAQ section
- [ ] Add progress bars for long operations
- [ ] Implement dry-run mode for testing

## Performance

- [ ] Profile and optimize merge operations
- [ ] Implement caching for repeated operations
- [ ] Add memory usage limits
- [ ] Optimize font loading/saving
- [ ] Parallelize independent operations
- [ ] Reduce temporary file usage
- [ ] Implement streaming for large fonts
- [ ] Add performance metrics logging

## Distribution

- [ ] Package for PyPI distribution
- [ ] Create Homebrew formula for macOS
- [ ] Create snap package for Linux
- [ ] Generate Windows installer
- [ ] Publish Docker image to Docker Hub
- [ ] Create conda package
- [ ] Set up GitHub Pages for documentation
- [ ] Create CDN for pre-merged fonts