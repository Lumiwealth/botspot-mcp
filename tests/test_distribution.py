import json
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
ENDPOINT = 'https://mcp.botspot.trade/mcp'


class DistributionContracts(unittest.TestCase):
    def test_claude_declares_its_existing_icon_and_privacy_policy(self):
        manifest = json.loads((ROOT / '.claude-plugin/plugin.json').read_text())
        self.assertEqual(manifest['privacyPolicyUrl'], 'https://botspot.trade/privacy')
        self.assertEqual(manifest['supportUrl'], 'https://botspot.trade/contact')
        self.assertEqual(manifest['documentationUrl'], 'https://botspot.trade/agents')
        self.assertEqual(manifest['displayName'], 'BotSpot')
        self.assertIn('free to connect', manifest['description'].lower())
        self.assertIn('trad', manifest['description'].lower())
        icon = ROOT / manifest['icon']
        self.assertTrue(icon.is_file())
        import struct
        data = icon.read_bytes()
        self.assertEqual(data[:8], b'\x89PNG\r\n\x1a\n')
        width, height = struct.unpack('>II', data[16:24])
        self.assertEqual(width, height)
        self.assertGreaterEqual(width, 512)
        self.assertLessEqual(width, 2048)
        self.assertLess(len(data), 2 * 1024 * 1024)

    def test_registry_metadata_preserves_identity_and_current_access(self):
        server = json.loads((ROOT / 'server.json').read_text())
        self.assertEqual(server['name'], 'io.github.grzesir/botspot-trading')
        self.assertEqual(server['remotes'], [{'type': 'streamable-http', 'url': ENDPOINT}])
        self.assertEqual(server['repository']['url'], 'https://github.com/Lumiwealth/botspot-mcp')
        self.assertLessEqual(len(server['description']), 100)
        self.assertIn('free to connect', server['description'].lower())

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

    def test_connecting_is_free_and_never_described_as_paid_only(self):
        # Rob, 2026-10-24: connecting the MCP is free and creates a free account.
        # Paid plans only unlock heavier features. Never say a paid plan is required to connect.
        texts = {
            'README.md': (ROOT / 'README.md').read_text(),
            'smithery.yaml': (ROOT / 'smithery.yaml').read_text(),
            'server.json': (ROOT / 'server.json').read_text(),
            'plugin.json': (ROOT / 'plugin.json').read_text(),
            '.claude-plugin/plugin.json': (ROOT / '.claude-plugin/plugin.json').read_text(),
        }
        for name, text in texts.items():
            lower = text.lower()
            for banned in ['paid botspot plan is required', 'paid botspot account is required',
                           'paid account required', 'paid plan required', 'paid botspot account required']:
                self.assertNotIn(banned, lower, name)
            self.assertIn('free', lower, name)

    def test_brand_asset_and_legal_metadata_are_available(self):
        manifest = json.loads((ROOT / 'plugin.json').read_text())
        interface = manifest['extensions']['com.openai']['interface']
        self.assertTrue((ROOT / interface['logo']).is_file())
        self.assertEqual(interface['privacyPolicyURL'], 'https://botspot.trade/privacy')
        self.assertEqual(interface['termsOfServiceURL'], 'https://botspot.trade/terms')
        self.assertTrue((ROOT / 'LICENSE').is_file())


if __name__ == '__main__':
    unittest.main()
