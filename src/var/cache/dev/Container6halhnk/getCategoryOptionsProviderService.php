<?php

use Symfony\Component\DependencyInjection\Argument\RewindableGenerator;

// This file has been auto-generated by the Symfony Dependency Injection Component for internal use.
// Returns the public 'PrestaShop\Module\PsxMarketingWithGoogle\ProductFilter\Options\CategoryOptionsProvider' shared service.

return $this->services['PrestaShop\\Module\\PsxMarketingWithGoogle\\ProductFilter\\Options\\CategoryOptionsProvider'] = new \PrestaShop\Module\PsxMarketingWithGoogle\ProductFilter\Options\CategoryOptionsProvider(${($_ = isset($this->services['PrestaShop\\Module\\PsxMarketingWithGoogle\\Repository\\CategoryRepository']) ? $this->services['PrestaShop\\Module\\PsxMarketingWithGoogle\\Repository\\CategoryRepository'] : $this->load('getCategoryRepository2Service.php')) && false ?: '_'});