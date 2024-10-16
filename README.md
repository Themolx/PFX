<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Custom Nuke Tools Documentation</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            line-height: 1.6;
            color: #333;
            max-width: 800px;
            margin: 0 auto;
            padding: 20px;
        }
        header {
            text-align: center;
            margin-bottom: 30px;
        }
        h1 {
            color: #2c3e50;
        }
        h2 {
            color: #34495e;
            border-bottom: 2px solid #ecf0f1;
            padding-bottom: 10px;
        }
        h3 {
            color: #16a085;
        }
        img {
            max-width: 100%;
            height: auto;
            display: block;
            margin: 0 auto;
        }
        a {
            color: #3498db;
            text-decoration: none;
        }
        a:hover {
            text-decoration: underline;
        }
        code {
            background-color: #f8f8f8;
            border: 1px solid #ddd;
            border-radius: 3px;
            padding: 2px 4px;
            font-family: Consolas, monospace;
        }
        pre {
            background-color: #f8f8f8;
            border: 1px solid #ddd;
            border-radius: 3px;
            padding: 10px;
            overflow-x: auto;
        }
    </style>
</head>
<body>
    <header>
        <img src="https://github.com/Themolx/PFX/blob/3468a4eb7451d9ecf24509e102c10c59c3d790dc/assets/PFX_Logo.png?raw=true" alt="PFX Logo">
        <h1>Custom Nuke Tools Documentation</h1>
        <p>By Martin Tomek</p>
    </header>

    <h2>Table of Contents</h2>
    <ul>
        <li><a href="#overview">Overview</a></li>
        <li><a href="#tools">Tools</a>
            <ul>
                <li><a href="#nuke-grab-tool">1. Nuke Grab Tool</a></li>
                <li><a href="#sequence-loader">2. Sequence Loader</a></li>
                <li><a href="#mask-checker">3. Mask Checker</a></li>
                <li><a href="#lock-cryptos">4. Lock Cryptos</a></li>
                <li><a href="#zdefocus-controller">5. ZDefocus Controller</a></li>
                <li><a href="#node-management-suite">6. Node Management Suite</a></li>
            </ul>
        </li>
        <li><a href="#installation">Installation</a></li>
        <li><a href="#conclusion">Conclusion</a></li>
    </ul>

    <h2 id="overview">Overview</h2>
    <p>As a Compositor and Technical Director, I've developed various tools to enhance workflow efficiency and solve common problems in Nuke compositing pipelines. This documentation outlines the functionality and benefits of each tool.</p>

    <h2 id="tools">Tools</h2>

    <h3 id="nuke-grab-tool">1. Nuke Grab Tool</h3>
    <ul>
        <li><strong>Problem Solved</strong>: Difficulty in organizing nodes when zoomed out</li>
        <li><strong>Key Features</strong>:
            <ul>
                <li>Blender-inspired 'grab' functionality</li>
                <li>Keyboard shortcut activation ('E')</li>
                <li>Confirm with left-click or Enter, cancel with Esc</li>
            </ul>
        </li>
    </ul>

    <h3 id="sequence-loader">2. Sequence Loader</h3>
    <ul>
        <li><strong>Problem Solved</strong>: Time-consuming manual import of multiple shots</li>
        <li><strong>Key Features</strong>:
            <ul>
                <li>Automatic sequence detection</li>
                <li>Multi-sequence support</li>
                <li>Consistent arrangement for review</li>
            </ul>
        </li>
    </ul>

    <h3 id="mask-checker">3. Mask Checker</h3>
    <ul>
        <li><strong>Problem Solved</strong>: Error-prone manual inspection of mask channels</li>
        <li><strong>Key Features</strong>:
            <ul>
                <li>Automated mask verification</li>
                <li>Grade node integration for enhanced visibility</li>
            </ul>
        </li>
    </ul>

    <h3 id="lock-cryptos">4. Lock Cryptos</h3>
    <ul>
        <li><strong>Problem Solved</strong>: Unexpected Cryptomatte layer changes causing errors</li>
        <li><strong>Key Features</strong>:
            <ul>
                <li>Automatic Cryptomatte detection</li>
                <li>Layer locking mechanism</li>
                <li>Dynamic labeling</li>
            </ul>
        </li>
    </ul>

    <h3 id="zdefocus-controller">5. ZDefocus Controller</h3>
    <ul>
        <li><strong>Problem Solved</strong>: Inconsistent management of multiple defocus nodes</li>
        <li><strong>Key Features</strong>:
            <ul>
                <li>Centralized control interface</li>
                <li>Automatic camera integration</li>
                <li>Render farm compatibility</li>
            </ul>
        </li>
    </ul>

    <h3 id="node-management-suite">6. Node Management Suite</h3>
    <p>An integrated suite of tools for enhanced node organization and management.</p>

    <h4>Dynamic Shuffle Labeler</h4>
    <ul>
        <li><strong>Problem Solved</strong>: Time-consuming manual labeling of Shuffle nodes</li>
        <li><strong>Key Features</strong>:
            <ul>
                <li>Automatic labeling with input channel</li>
                <li>Postage stamp activation for non-RGBA shuffles</li>
                <li>Automatic keep node for RGBA channels</li>
            </ul>
        </li>
    </ul>

    <h4>CryptoLabel Tool</h4>
    <ul>
        <li><strong>Problem Solved</strong>: Unclear labeling and RGBA output issues in CryptoMatte nodes</li>
        <li><strong>Key Features</strong>:
            <ul>
                <li>Dynamic labeling with layer and matte information</li>
                <li>Automatic RGBA preservation</li>
                <li>Intelligent node positioning</li>
            </ul>
        </li>
    </ul>

    <h4>Animated Node Labeler</h4>
    <ul>
        <li><strong>Problem Solved</strong>: Difficulty in identifying animated nodes</li>
        <li><strong>Key Features</strong>:
            <ul>
                <li>Automatic animation detection</li>
                <li>Mix value display</li>
                <li>Color coding for easy identification</li>
                <li>Toggleable functionality</li>
            </ul>
        </li>
    </ul>

    <h2 id="installation">Installation</h2>
    <ol>
        <li>Download the tools package</li>
        <li>Place scripts in your Nuke plugins directory</li>
        <li>Add to your <code>init.py</code>:</li>
    </ol>
    <pre><code>nuke.pluginAddPath("/path/to/custom_tools")</code></pre>
    <ol start="4">
        <li>Restart Nuke</li>
    </ol>

    <h2 id="conclusion">Conclusion</h2>
    <p>These tools represent a comprehensive approach to solving common VFX production challenges. They offer significant time savings, improved consistency, and enhanced quality control in daily tasks. As a Technical Director, I remain committed to refining and expanding this toolkit based on user feedback and evolving production needs.</p>
    <p>Feel free to reach out with questions, suggestions, or specific workflow challenges that might benefit from similar custom solutions.</p>
</body>
</html>
