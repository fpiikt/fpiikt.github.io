<?php
use Slim\Interfaces\ErrorRendererInterface;

class MyCustomErrorRenderer implements ErrorRendererInterface
{
    public function __invoke(Throwable $exception, bool $displayErrorDetails): string
    {
        return 'Пока нет';
    }
}