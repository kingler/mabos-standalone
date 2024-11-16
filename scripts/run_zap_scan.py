import time
import os
import sys
import logging
from zapv2 import ZAPv2
from datetime import datetime

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# Replace with the actual path to your ZAP installation
ZAP_PATH = '/path/to/zap/installation'

# The URL of the application we want to test
TARGET = 'https://localhost:3000'

# Path to ZAP configuration file
ZAP_CONFIG_PATH = 'config/zap-config.conf'

def load_zap_config(config_path):
    config = {}
    try:
        with open(config_path, 'r') as f:
            for line in f:
                line = line.strip()
                if line and not line.startswith('#'):
                    key, value = line.split('=', 1)
                    config[key.strip()] = value.strip()
    except FileNotFoundError:
        logger.error(f"ZAP configuration file not found: {config_path}")
        sys.exit(1)
    except Exception as e:
        logger.error(f"Error reading ZAP configuration: {str(e)}")
        sys.exit(1)
    return config

def run_zap_scan():
    try:
        # Load ZAP configuration
        zap_config = load_zap_config(ZAP_CONFIG_PATH)

        # Set up ZAP
        zap = ZAPv2(proxies={'http': 'http://localhost:8080', 'https': 'http://localhost:8080'})

        # Start ZAP
        logger.info('Starting ZAP ...')
        os.system(f'{ZAP_PATH} -daemon -config api.disablekey=true -config {ZAP_CONFIG_PATH} &')
        time.sleep(20)  # Give ZAP time to start

        # Access the target
        logger.info(f'Accessing target {TARGET}')
        zap.urlopen(TARGET)
        time.sleep(2)  # Give the site a chance to respond

        logger.info('Spidering target ...')
        scanid = zap.spider.scan(TARGET)
        # Give the Spider a chance to start
        time.sleep(2)
        while (int(zap.spider.status(scanid)) < 100):
            logger.info(f'Spider progress {zap.spider.status(scanid)}%')
            time.sleep(2)

        logger.info('Spider completed')

        # Wait for passive scanning to complete
        while (int(zap.pscan.records_to_scan) > 0):
            logger.info(f'Records to passive scan {zap.pscan.records_to_scan}')
            time.sleep(2)

        logger.info('Passive scanning completed')

        logger.info('Starting active scan ...')
        scanid = zap.ascan.scan(TARGET)
        while (int(zap.ascan.status(scanid)) < 100):
            logger.info(f'Scan progress {zap.ascan.status(scanid)}%')
            time.sleep(5)

        logger.info('Active scan completed')

        # Generate report
        logger.info('Generating report ...')
        timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
        report_html = zap.core.htmlreport()
        report_path = f'security_reports/zap_report_{timestamp}.html'
        os.makedirs(os.path.dirname(report_path), exist_ok=True)
        with open(report_path, 'w') as f:
            f.write(report_html)

        logger.info(f'Report saved to {report_path}')

        # List alerts
        logger.info('Alerts:')
        alerts = zap.core.alerts()
        for alert in alerts:
            logger.info(f'- {alert["alert"]} [{alert["risk"]}]')

        # Shutdown ZAP
        zap.core.shutdown()
        logger.info('ZAP has been shutdown')

    except Exception as e:
        logger.error(f"An error occurred during the ZAP scan: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    run_zap_scan()