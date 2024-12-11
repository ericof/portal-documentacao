// Glossario
import { Tooltips } from '@rohberg/volto-slate-glossary/components';

const applyConfig = (config) => {
  config.settings.isMultilingual = false;
  config.settings.supportedLanguages = ['pt-br'];
  config.settings.defaultLanguage = 'pt-br';
  config.settings.appExtras = [
    ...config.settings.appExtras,
    {
      match: '/',
      component: Tooltips,
    },
  ];
  // Glossary
  config.settings.glossary.matchOnlyFirstOccurence = true;
  config.settings.glossary.mentionTermInTooltip = true;
  return config;
};

export default applyConfig;
