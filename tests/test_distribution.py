import json
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
ENDPOINT = 'https://mcp.botspot.trade/mcp'


class DistributionContracts(unittest.TestCase):
    def test_openai_public_summary_meets_submission_limit(self):
        manifest = json.loads((ROOT / 'plugin.json').read_text())
        summary = manifest['extensions']['com.openai']['interface']['shortDescription']
        self.assertTrue(summary.strip())
        self.assertLessEqual(len(summary), 30)

    def test_portable_plugin_has_a_remote_connection(self):
        manifest = json.loads((ROOT / 'plugin.json').read_text())
        self.assertEqual(manifest['name'], 'botspot')
        config = json.loads((ROOT / 'mcp.json').read_text())
        self.assertEqual(config['mcpServers']['botspot']['type'], 'streamable-http')
        self.assertEqual(config['mcpServers']['botspot']['url'], ENDPOINT)

    def test_grok_and_claude_use_the_same_connection(self):
        manifest = json.loads((ROOT / '.claude-plugin/plugin.json').read_text())
        self.assertEqual(manifest['name'], 'botspot')
        config = json.loads((ROOT / manifest['mcpServers']).read_text())
        self.assertEqual(config['mcpServers']['botspot']['url'], ENDPOINT)
        self.assertEqual(config['mcpServers']['botspot']['type'], 'http')

    def test_public_configuration_contains_no_credentials_or_hooks(self):
        for name in ['plugin.json', 'mcp.json', '.mcp.json', '.claude-plugin/plugin.json']:
            value = json.loads((ROOT / name).read_text())
            content = json.dumps(value).lower()
            for forbidden in ['authorization', 'clientsecret', 'password', 'hooks', 'command']:
                self.assertNotIn(forbidden, content, name)

    def test_retired_connection_and_free_offer_are_not_advertised(self):
        for name in ['README.md', 'smithery.yaml']:
            text = (ROOT / name).read_text().lower()
            for retired in ['/mcp/public', 'free tier', 'no credit card required', 'generate_strategy', 'refine_strategy']:
                self.assertNotIn(retired, text, name)

    def test_brand_asset_and_legal_metadata_are_available(self):
        manifest = json.loads((ROOT / 'plugin.json').read_text())
        interface = manifest['extensions']['com.openai']['interface']
        self.assertTrue((ROOT / interface['logo']).is_file())
        self.assertEqual(interface['privacyPolicyURL'], 'https://botspot.trade/privacy')
        self.assertEqual(interface['termsOfServiceURL'], 'https://botspot.trade/terms')
        self.assertTrue((ROOT / 'LICENSE').is_file())


if __name__ == '__main__':
    unittest.main()
