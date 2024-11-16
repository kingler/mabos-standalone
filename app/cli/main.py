"""CLI entry point for the MABOS terminal interface."""
import asyncio
from typing import Optional
import typer
from app.interfaces.terminal_interface import TerminalInterface
from app.services.mabos_service import MABOSService
from app.services.erp_service import ERPService
from app.db.arango_db_client import ArangoDBClient
from app.config.config import CONFIG

app = typer.Typer()

async def setup_services() -> tuple[ArangoDBClient, ERPService, MABOSService]:
    """Initialize required services.
    
    Returns:
        Tuple containing initialized db_client, erp_service, and mabos_service
    """
    # Initialize database client
    db_client = ArangoDBClient(
        host=CONFIG.ARANGO_HOST,
        port=CONFIG.ARANGO_PORT,
        username=CONFIG.ARANGO_USER,
        password=CONFIG.ARANGO_PASSWORD,
        database=CONFIG.ARANGO_DATABASE
    )
    
    # Initialize ERP service
    erp_service = ERPService()
    
    # Initialize MABOS service with required components using factory method
    mabos_service = await MABOSService.create(
        erp_service=erp_service,
        modeling_service=CONFIG.modeling_service,
        num_agents=CONFIG.num_agents,
        num_states=CONFIG.num_states,
        state_size=CONFIG.state_size,
        action_size=CONFIG.action_size,
        ontology_path=CONFIG.ontology_path
    )
    
    # Initialize MABOS service asynchronously
    await mabos_service.initialize()
    
    return db_client, erp_service, mabos_service

async def async_main(debug: bool = False):
    """Async main function to handle all async operations."""
    try:
        # Initialize services
        db_client, erp_service, mabos_service = await setup_services()
        
        # Create and start terminal interface
        terminal = TerminalInterface(
            db_client=db_client,
            erp_service=erp_service,
            mabos_service=mabos_service
        )
        
        # Start conversation loop
        await terminal.start_conversation()
        
    except Exception as e:
        if debug:
            raise
        typer.echo(f"Error: {str(e)}", err=True)
        raise typer.Exit(1)

@app.command()
def start(
    debug: bool = typer.Option(False, "--debug", "-d", help="Enable debug mode")
) -> None:
    """Start the MABOS terminal interface."""
    try:
        # Run the async main function
        asyncio.run(async_main(debug))
    except Exception as e:
        if debug:
            raise
        typer.echo(f"Error: {str(e)}", err=True)
        raise typer.Exit(1)

if __name__ == "__main__":
    app()
